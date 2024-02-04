from pytube import YouTube
import os


def download_video(url, output_path="downloads/"):
    """Download a video from YouTube by URL.

    Args:
        url (str): The URL of the YouTube video to download.
        output_path (str): The directory where the video will be saved.

    Returns:
        str: The filename of the downloaded video.
    """
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return video.download(output_path=output_path)


# Optionally, you could include more functionality here, such as:
# - A function to extract audio from the downloaded video.
# - Functions to handle specific video formats or qualities.
