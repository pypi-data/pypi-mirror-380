import os

from huggingface_hub import snapshot_download, hf_hub_download
import tensorflow as tf
import numpy as np
import pandas as pd
from scipy.special import expit
import soundfile as sf

from monkeycall.helper import chunk_with_padding, load_audio_representation, z_norm, predictions_to_df, get_audio_files, ensure_dir
from monkeycall.custom_objects.spider_monkey_custom_objects import custom_objects


def load_model(
    architecture: str = "georgiosrizos/spider-monkey-detector-SEResNet",
    cache_dir: str | None = None  # TODO: To implement this.
):
    """
        Load a pre-trained spider monkey call detection model.

        Args:
            architecture: Model architecture name (e.g., "georgiosrizos/spider-monkey-dummy-detector").
            cache_dir: Local directory to cache downloaded weights.

        Returns:
            A tensorflow inference model.
        """

    if cache_dir is not None:
        raise NotImplementedError("Need to implement.")

    # This will create a local cache folder and return its path
    if architecture == "georgiosrizos/spider-monkey-detector-SEResNet":
        model_dir = hf_hub_download(repo_id=architecture, filename="spider-monkey-detector-SEResNet.keras")
    # elif architecture == "georgiosrizos/spider-monkey-dummy-detector":
    #     model_dir = snapshot_download(architecture)
    else:
        raise ValueError("Model architecture not found.")

    print(f"Model files downloaded to: {model_dir}")

    # Load the SavedModel with TensorFlow.
    if architecture == "georgiosrizos/spider-monkey-detector-SEResNet":
        model = tf.keras.models.load_model(model_dir, custom_objects=custom_objects, compile=False)
    # elif architecture == "georgiosrizos/spider-monkey-dummy-detector":
    #     model = tf.saved_model.load(model_dir)
    #     model = model.signatures["serving_default"]
    else:
        raise ValueError("Model architecture not found.")

    return model


def predict_3_sec_clip(
    audio_path: str,
    model=None,
) -> dict | np.float32:
    """
    Run inference on an audio file.

    Args:
        audio_path: Path to WAV file.
        model: Preloaded model (optional). If None, loads default pretrained model.

    Returns:
        - prediction_probability: float the probability a whinny has been detected in this 3 sec clip.
    """
    _, logmel_spectrogram, custom_stats = load_audio_representation(audio_path)

    if logmel_spectrogram.shape[0] < 300:
        # Sample-scope z-norm
        logmel_spectrogram = z_norm(logmel_spectrogram, custom_stats)

        # Pad.
        logmel_spectrogram = np.pad(
            logmel_spectrogram,
            pad_width=((0, 300 - logmel_spectrogram.shape[0]), (0, 0)),  # (rows, cols)
            mode="constant",
            constant_values=0
        )
    elif logmel_spectrogram.shape[0] > 300:
        raise ValueError("This recording is more than 3 sec long. Please try the predict_recording() function instead.")
    else:
        pass

    # outputs = model(tf.constant(logmel_spectrogram.reshape((1,
    #                                                         logmel_spectrogram.shape[0],
    #                                                         logmel_spectrogram.shape[1]))))["output"]

    outputs = model.predict(logmel_spectrogram.reshape((1,
                                                logmel_spectrogram.shape[0],
                                                logmel_spectrogram.shape[1])),
                            verbose=0)

    # outputs = tf.nn.sigmoid(outputs).numpy()  # Activate the logit to get prediction probability.
    outputs = expit(outputs)  # Activate the logit to get prediction probability.

    # return float(outputs[0, 0])
    return outputs[0, 0]


def predict_recording(
    audio_path: str,
    model=None,
    hop_size: int | None = 1,
    probability_threshold: float | None = 0.5,
    output_folder: str | None = None
) -> dict | pd.DataFrame:
    """
        Run inference on an audio file.

        Args:
            audio_path: Path to WAV file.
            model: Preloaded model (optional). If None, loads default pretrained model.
            hop_size: Step size (in seconds) for windowing. Defaults to window_size.
            probability_threshold: Clips with prediction probability higher than this, will be considered positive.
            output_folder: Path to folder to store positive audio clip files.

        Returns:
            - DataFrame with columns [timestamp_start, timestamp_end, prob_positive].
        """
    waveform, logmel_spectrogram, custom_stats = load_audio_representation(audio_path)

    file_name = os.path.splitext(os.path.basename(audio_path))[0]

    # Pad or do windowing.
    if logmel_spectrogram.shape[0] <= 300:
        raise ValueError("This is a 3 sec long recording. Please try the predict_3_sec_clip() function instead.")
    else:
        # Windowing.
        window_size_frames = 300
        hop_size_frames = 100 * hop_size

        clip_list, custom_stats_list = chunk_with_padding(logmel_spectrogram, window=window_size_frames, hop=hop_size_frames)
        for i in range(len(clip_list)):
            clip_list[i] = z_norm(clip_list[i], custom_stats_list[i])

    output_list = list()
    for clip_id, clip in enumerate(clip_list):
        # outputs = model(tf.constant(clip.reshape((1,
        #                                           clip.shape[0],
        #                                           clip.shape[1]))))["output"]
        #
        # outputs = tf.nn.sigmoid(outputs).numpy()  # Activate the logit to get prediction probability.
        # output_list.append(float(outputs[0, 0]))
        outputs = model.predict(clip.reshape((1,
                                              clip.shape[0],
                                              clip.shape[1])),
                                verbose=0)

        outputs = expit(outputs)  # Activate the logit to get prediction probability.
        output_list.append(outputs[0, 0])

        if output_folder is not None:
            if outputs[0, 0] > probability_threshold:
                if waveform.size < (clip_id * 16000 * hop_size) + 48000:
                    clip_waveform = waveform[clip_id * 16000 * hop_size:]
                else:
                    clip_waveform = waveform[clip_id * 16000 * hop_size: (clip_id * 16000 * hop_size) + 48000]

                sf.write(os.path.join(output_folder, file_name + "_" + repr(int(clip_id * hop_size)) + "_" + repr(int(clip_id * hop_size) + 3) + ".wav"), clip_waveform, 16000)

    data_frame = predictions_to_df(probs=output_list,
                                   clip_duration=3,
                                   hop=hop_size,
                                   audio_path=audio_path)

    return data_frame


def search_folder_for_calls(
    input_folder: str,
    model=None,
    hop_size: int | None = 1,
    probability_threshold: float | None = 0.5,
    output_folder: str | None = None,
    extensions: tuple | None = (".wav", ".WAV", ".mp3", ".MP3", ".flac", ".FLAC", ".ogg", ".OGG")
) -> dict | pd.DataFrame:
    """
        Run inference on multiple audio files in a folder.

        Args:
            input_folder: Path to folder containing multiple WAV only files.
            model: Preloaded model (optional). If None, loads default pretrained model.
            hop_size: Step size (in seconds) for windowing. Defaults to window_size.
            probability_threshold: Clips with prediction probability higher than this, will be considered positive.
            output_folder: Path to folder to store positive audio clip files.
            extensions: the audio file extensions to look for in the folder.


        Returns:
            - DataFrame with columns [timestamp_start, timestamp_end, prob_positive].
    """

    if output_folder is not None:
        # Create output folder if it doesn't exist yet.
        ensure_dir(output_folder)

    # file_names = os.listdir(input_audio_folder)
    file_names = get_audio_files(input_folder, extensions=extensions)
    file_paths = [os.path.join(input_folder, file_name) for file_name in file_names]

    if len(file_paths) == 0:
        raise ValueError("No audio files found in input folder. Check folder and extensions to search for.")

    data_frame_list = list()
    for file_name, file_path in zip(file_names, file_paths):
        print("Now processing file:", file_name)
        data_frame = predict_recording(audio_path=file_path,
                                       model=model,
                                       hop_size=hop_size,
                                       probability_threshold=probability_threshold,
                                       output_folder=output_folder)
        data_frame_list.append(data_frame)
    output_df = pd.concat(data_frame_list, ignore_index=True)

    return output_df
