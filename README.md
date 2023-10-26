# PDF to PNG Converter

This is a simple Python application built with tkinter that allows you to convert individual pages of a PDF file into PNG images. You can specify the page number to convert and the output directory for the generated PNG files.

## Features

- Select a PDF file for conversion.
- Input the page number you want to convert.
- Choose an output directory for the PNG files.
- Start the conversion process, which runs in a separate thread.
- View progress with a progress bar.
- Error handling for invalid inputs and file issues.

## Prerequisites

Before using this application, you need to have the following dependencies installed:

- Python 3.x
- tkinter
- pdf2image
- PyPDF2

You can install these dependencies using pip:

pip install tkinter pdf2image PyPDF2


## Usage

1. Launch the application by running `pdf_to_png_converter.py`.

2. Click the "Select PDF" button to choose the PDF file you want to convert.

3. Enter the page number (1-indexed) you want to convert in the "Enter Page Number" field.

4. Click the "Select Output Directory" button to specify where you want to save the PNG file.

5. Click the "Convert" button to start the conversion process. The progress bar will show the conversion progress.

6. Once the conversion is complete, a message box will notify you of the completion.

## Contributing

If you have suggestions, improvements, or bug fixes, please feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
