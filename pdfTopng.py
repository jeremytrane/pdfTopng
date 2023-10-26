import sys
import tkinter as tk
from tkinter import messagebox, filedialog
from pdf2image import convert_from_path
import PyPDF2

def get_pdf_page_count(pdf_path):
    """Return the number of pages in the given PDF."""
    with open(pdf_path, 'rb') as f:
        pdf = PyPDF2.PdfReader(f)
        print(f"Number of pages in the pdf: {len(pdf.pages)}")
        return len(pdf.pages)

def convert_pdf():
    if not pdf_file_path.get():
        messagebox.showerror("Error", "No PDF file provided!")
        return

    # Fetch the user input page number
    try:
        page_num = int(page_number_entry.get()) - 1
        print(f"Page to convert: {page_num + 1}")
    except ValueError:
        messagebox.showerror("Error", "Invalid page number!")
        return

    path = pdf_file_path.get()
    print(f"Path to convert: {path}")
    
    # Check if the provided page number is within the range
    total_pages = get_pdf_page_count(path)
    if page_num < 0 or page_num >= total_pages:
        messagebox.showerror("Error", f"Page number out of range! PDF has {total_pages} pages.")
        return

    images = convert_from_path(path)

    # Only convert the specified page number
    images[page_num].save(f'Downloads/output_page_{page_num + 1}.png', 'PNG')
    
    messagebox.showinfo("Info", "Conversion Complete!")


def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_file_path.set(file_path)
        print(f"Selected file: {file_path}")
        selected_file_label.config(text=file_path.split("/")[-1])

root = tk.Tk()
root.title("PDF to PNG Converter")

pdf_file_path = tk.StringVar()

btn_select = tk.Button(root, text="Select PDF", command=select_pdf)
btn_select.pack(pady=10)

# Add a label to display the selected file name
selected_file_label = tk.Label(root, text="", font=("Arial", 10))
selected_file_label.pack(pady=5)

# Add an Entry widget for page number input
page_number_label = tk.Label(root, text="Enter Page Number:", font=("Arial", 10))
page_number_label.pack(pady=5)
page_number_entry = tk.Entry(root)
page_number_entry.pack(pady=5)

btn_convert = tk.Button(root, text="Convert", command=convert_pdf)
btn_convert.pack(pady=20)

root.mainloop()
