import moviepy.editor
from pathlib import Path


def extract_mp3(file_path):
    video_file = Path(file_path)
    video = moviepy.editor.VideoFileClip(f'{video_file}')
    audio = video.audio
    audio_file = f'{video_file.stem}.mp3'
    audio.write_audiofile(audio_file)
    return audio_file


if __name__ == '__main__':
    extract_mp3(file_path='video.mp4')
