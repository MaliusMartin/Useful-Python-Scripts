# Resize Image

This script allows you to resize image files to specified dimensions, making it useful for optimizing images for web use, saving storage space, or meeting specific resolution requirements.

---

## Features

- Resizes images to the desired width and height.
- Supports multiple image formats like PNG, JPEG, etc.
- Uses the `Pillow` library for efficient image processing.

---

## Requirements

Install the required library before running the script:

```bash
pip install pillow
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `input_image` variable with the path to your image file.
3. Set the desired `new_width` and `new_height`.
4. Run the script:

   ```bash
   python resize_image.py
   ```

5. The resized image will be saved in the same directory as the input file with `_resized` appended to its name.

---

## Example Code

```python
from PIL import Image

# Input image file path
input_image = "path/to/input_image.jpg"

# Output image file path
output_image = "path/to/output_image_resized.jpg"

# Desired dimensions
new_width = 800
new_height = 600

# Open the image file
with Image.open(input_image) as img:
    # Resize the image
    resized_img = img.resize((new_width, new_height))
    
    # Save the resized image
    resized_img.save(output_image)

print(f"Resized image saved as: {output_image}")
```

---

## Output

The script resizes the input image to the specified dimensions and saves it as a new file. The output file is optimized for the desired resolution.

---

## Customization

- **Aspect Ratio**: To maintain the original aspect ratio, calculate one dimension (width or height) based on the other using the original aspect ratio.
- **Image Format**: Save the resized image in a different format (e.g., PNG, JPEG) by changing the file extension and format parameter in the `save` method.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

