# Convert Doc to PDF

This script enables you to convert Microsoft Word documents (`.doc` or `.docx`) into PDF files. It is particularly useful for batch conversions or automated workflows.

---

## Features

- Supports `.doc` and `.docx` formats.
- Converts Word files to PDF with high fidelity.
- Simple and easy-to-use script.

---

## Requirements

Install the required libraries before running the script:

```bash
pip install python-docx
pip install fpdf
```

---

## How to Use

1. Clone the repository or download the script to your local machine.
2. Ensure the `.doc` or `.docx` file you want to convert is in the same directory as the script.
3. Run the script and provide the name of the Word document:

   ```bash
   python convert_doc_to_pdf.py
   ```

4. The converted PDF will be saved in the same directory.

---

## Example Code

```python
from docx import Document
from fpdf import FPDF

# Specify the input and output file names
input_file = "example.docx"
output_file = "example.pdf"

# Load the Word document
doc = Document(input_file)

# Initialize the PDF object
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add content from the Word document to the PDF
for paragraph in doc.paragraphs:
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, paragraph.text)

# Save the PDF
pdf.output(output_file)

print(f"{output_file} has been created successfully!")
```

---

## Output

The script generates a PDF file (`example.pdf`) that contains the text and formatting of the original Word document.

---

## Customization

- **Font and Size**: Change the font style and size in the `pdf.set_font()` method.
- **Page Layout**: Modify margins or add headers and footers by extending the script.
- **Batch Conversion**: Enhance the script to process multiple `.docx` files in a directory.

---

## License

This script is part of the **Useful Python Scripts** repository and is licensed under the MIT License.

---

Happy coding!

