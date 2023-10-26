# PDF to PNG Converter with GUI

This simple GUI-based application allows users to convert a specific page of a PDF file into a PNG image. Built with Python's `tkinter` for the GUI interface and `pdf2image` for the conversion functionality.

![upload](https://github.com/jeremytrane/pdfTopng/assets/114171300/5bf5f236-56fc-4c5a-95cf-a67d274b9a77)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (3.x recommended)
- `tkinter` (usually bundled with Python's standard library)
- `pdf2image`
- `poppler-utils` (needed by `pdf2image`)

## Installation

1. **Clone this repository**:
   
   ```bash
   git clone https://github.com/your-username/pdf-to-png-converter.git

Navigate to the cloned directory:

cd pdf-to-png-converter

Install the necessary libraries:

pip install pdf2image

For Linux users, ensure you have poppler-utils installed:

sudo apt-get install poppler-utils

Usage
Run the application:

Copy code
python pdf_to_png_gui.py
Select a PDF: Click the Select PDF button and choose your desired PDF file.

Specify the Page Number: Enter the page number you want to convert.

Convert: Click the Convert button. The selected page will be converted into a PNG and saved in the Downloads folder as output_page_[page_number].png.

Contributing
Contributions are welcome! Please feel free to fork this repository, make your changes, and then submit a pull request.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
