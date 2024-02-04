from pytube import YouTube
import os


def download_video(url, output_path="downloads/"):
    """
    Download the video from the given URL and save it to the output_path.
    Returns the filename of the downloaded video.
    """
    yt = YouTube(url)
    video = yt.streams.filter(progressive=True, file_extension="mp4").first()
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return video.download(output_path=output_path)


def convert_video_to_audio(video_path, output_format="wav"):
    """
    Convert the downloaded video to an audio file with the specified format.
    Returns the filename of the converted audio file.
    """
    # Conversion logic goes here. You can use moviepy or call FFmpeg directly.
    # This is just a placeholder function to illustrate the concept.
    pass
