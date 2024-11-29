import pytube
from moviepy.editor import *

video_url = 'https://youtu.be'


yt = pytube.YouTube(video_url)


stream = yt.streams.filter(only_audio=True).first()


audio_path = stream.download('path/to/download/folder')


audio = AudioFileClip(audio_path)
audio_mp3_path = audio_path[:-4] + '.mp3'
audio.write_audiofile(audio_mp3_path)


audio.close()
os.remove(audio_path)

print(f"Audio downloaded and converted to MP3: {audio_mp3_path}")
