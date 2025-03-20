from pytubefix import YouTube
import os

def baixar_video(url: str):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(file_extension="mp4").get_highest_resolution()

        download_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "downloads")
        os.makedirs(download_path, exist_ok=True)

        file_path = os.path.join(download_path, yt.title + ".mp4")
        stream.download(output_path=download_path, filename=yt.title + ".mp4")

        return file_path

    except Exception as e:
        return str(e)
