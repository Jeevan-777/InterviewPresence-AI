import librosa
import numpy as np
from moviepy import VideoFileClip

def analyze_audio(video_path):
    audio_path = video_path.replace(".webm", ".wav")

    # extract audio
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)

    # load audio
    y, sr = librosa.load(audio_path)

    # split speech and silence
    intervals = librosa.effects.split(y, top_db=30)

    speech_duration = sum(
        (end - start) for start, end in intervals
    ) / sr

    total_duration = librosa.get_duration(y=y, sr=sr)

    silence_duration = total_duration - speech_duration

    speech_percent = (speech_duration / total_duration) * 100

    return speech_percent, silence_duration, total_duration

