from pytube import YouTube

video_url = 'URL of the video to download'

download_path = 'Path to save the downloaded video'

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

stream.download(output_path=download_path)
print("Video downloaded successfully!")