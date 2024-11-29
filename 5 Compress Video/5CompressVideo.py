from moviepy.editor import VideoFileClip

def compress_video(input_path, output_path, bitrate='1000k'):
  try:
    clip = VideoFileClip(input_path)

    if clip is None:
      raise ValueError(f"Failed to load video from '{input_path}'")

    moviepy_version = float(__version__)
    if moviepy_version >= 0.88:
      resized_clip = clip.resize(scale=0.5)  
    else:
      resized_clip = clip.resize(width=clip.size[0] // 2, height=clip.size[1] // 2)

    if resized_clip is None:
      raise ValueError("Failed to resize video")

    # Compressing the video
    resized_clip.write_videofile(output_path, bitrate=bitrate)

    print(f"Video compression successful. Output saved to '{output_path}'")

  except Exception as e:
    print(f"Error: {e}")

input_file = 'path/to/input_video.mp4'
output_file = 'path/to/compressed_video.mp4'
compress_video(input_file, output_file)
