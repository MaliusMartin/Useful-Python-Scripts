# Compress Video

This script allows you to compress video files, reducing their size without significant loss of quality. It uses the `moviepy` library to make the process simple and efficient.

---

## Features

- Compresses video files to reduce file size.
- Retains good video quality while minimizing size.
- Easy to use and customize for different resolutions and bitrates.

---

## Requirements

Install the required library before running the script:

```bash
pip install moviepy
```

Ensure that `ffmpeg` is installed on your system. You can download it from [ffmpeg.org](https://ffmpeg.org/).

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `input_video` variable with the path to your video file.
3. Run the script:

   ```bash
   python compress_video.py
   ```

4. The compressed video will be saved in the same directory as the input file.

---

## Example Code

```python
from moviepy.video.io.VideoFileClip import VideoFileClip

# Input video file path
input_video = "path/to/input_video.mp4"

# Output video file path
output_video = "path/to/output_video.mp4"

# Open the video file
clip = VideoFileClip(input_video)

# Compress the video by resizing (example: resize to 720p)
clip_resized = clip.resize(height=720)

# Write the compressed video to the output file
clip_resized.write_videofile(output_video, codec='libx264', bitrate='500k')

print(f"Compressed video saved as: {output_video}")
```

---

## Output

The script compresses the input video and saves it as a new file. The output file is smaller in size, making it easier to store and share.

---

## Customization

- **Resolution**: Adjust the `resize` method to set a specific resolution, such as 480p or 1080p.
- **Bitrate**: Modify the `bitrate` parameter in the `write_videofile` method to control the video quality and size.
- **Codec**: Change the `codec` to use a different video encoding standard if needed.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

