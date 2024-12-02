# YouTube Video Downloader

This script enables you to download videos from YouTube directly to your local machine. It leverages the `pytube` library for fetching video content and saving it in a specified format.

---

## Features

- Download YouTube videos with ease.
- Supports various resolutions based on video availability.
- Simple and customizable.

---

## Requirements

Install the required library before running the script:

```bash
pip install pytube
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `video_url` variable with the URL of the YouTube video you wish to download.
3. Run the script:

   ```bash
   python yt_video_download.py
   ```

4. The video will be downloaded and saved in the specified directory.

---

## Example Code

```python
from pytube import YouTube

# YouTube video URL
video_url = 'https://youtu.be/your_video_link_here'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams.get_highest_resolution()

# Download the video
output_path = 'path/to/save/directory'
stream.download(output_path)

print(f"Video downloaded successfully to {output_path}")
```

---

## Output

The script downloads the selected YouTube video and saves it to the specified directory with the original file name.

---

## Customization

- **Resolution**: Use `yt.streams.filter(res="resolution_here").first()` to download videos of a specific resolution.
- **Format**: Modify the `streams` filter to choose between audio or video formats.
- **Output Directory**: Change the `output_path` variable to specify where the downloaded file should be saved.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

