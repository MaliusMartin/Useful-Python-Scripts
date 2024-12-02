# Generate QR Code

This script allows you to create QR codes for URLs, text, or other types of data. The QR code is saved as an image file (.png), which can be used for sharing information visually.

---

## Features

- Generate QR codes for any type of data.
- Customize the size and error correction level of the QR code.
- Save the generated QR code as an image file.

---

## Requirements

Install the required library before running the script:

```bash
pip install qrcode
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Replace the `data` variable with the content you want to encode in the QR code.
3. Run the script:

   ```bash
   python generate_qr_code.py
   ```

4. The QR code will be generated and saved as `qr_code1.png` in the same directory.

---

## Example Code

```python
import qrcode

data = "https://github.com/MaliusMartin/MiniProjects-Electronincs/tree/main/12V%20DC%20Pump"

qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code (1 is the smallest).
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level.
    box_size=10  # Size of each box in pixels.
)

qr.add_data(data)
qr.make(fit=True)  # Ensures the QR Code is compact.

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr_code1.png")

print("QR code generated successfully!")
```

---

## Output

The script saves the QR code as an image file (`qr_code1.png`).

### Example Output:

![QR Code Example]qr_code1.png) 

---

## Customization

You can customize the following parameters:

- **Data**: Change the `data` variable to encode different content.
- **Version**: Adjust the QR code's size by modifying the `version` parameter.
- **Error Correction**: Use different error correction levels (`ERROR_CORRECT_L`, `M`, `Q`, or `H`).
- **Colors**: Customize `fill_color` and `back_color` for different color schemes.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

