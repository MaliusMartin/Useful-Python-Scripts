# Download Audio from YouTube

This script allows you to download the audio from a YouTube video and save it as an MP3 file. It is useful for extracting audio tracks from videos for offline listening or other purposes.

---

## Features

- Downloads audio directly from YouTube videos.
- Converts the downloaded audio to MP3 format.
- Deletes the original downloaded file to save space.

---

## Requirements

Install the required libraries before running the script:

```bash
pip install pytube moviepy
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `video_url` variable with the URL of the YouTube video.
3. Run the script:

   ```bash
   python download_audio_from_youtube.py
   ```

4. The MP3 file will be saved in the specified directory.

---

## Example Code

```python
import pytube
from moviepy.editor import AudioFileClip
import os

# YouTube video URL
video_url = 'https://youtu.be/example_video_url'

# Create a YouTube object
yt = pytube.YouTube(video_url)

# Get the audio stream
stream = yt.streams.filter(only_audio=True).first()

# Download the audio
audio_path = stream.download('path/to/save')

# Convert the audio to MP3
audio = AudioFileClip(audio_path)
audio_mp3_path = audio_path[:-4] + '.mp3'
audio.write_audiofile(audio_mp3_path)

# Delete the original audio file
audio.close()
os.remove(audio_path)

print(f"Audio downloaded and converted to MP3: {audio_mp3_path}")
```

---

## Output

The script downloads the audio from the specified YouTube video and saves it as an MP3 file in the given directory.

---

## Troubleshooting

1. **HTTP Error 403**:
   - This error occurs when the YouTube video is restricted or age-gated.
   - Consider using additional libraries like `yt-dlp` to bypass such restrictions.

2. **`moviepy` Warnings**:
   - Ensure `ffmpeg` is installed and properly configured on your system.
   - You can download `ffmpeg` from [ffmpeg.org](https://ffmpeg.org/).

---

## Customization

- **Save Directory**: Change the download directory by modifying the `stream.download('path/to/save')` line.
- **Audio Format**: Use different audio formats by modifying the `AudioFileClip` output settings.
- **Batch Processing**: Extend the script to download audio from multiple YouTube URLs.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

