import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from pdf2image import convert_from_path
import PyPDF2
import threading

def get_pdf_page_count(pdf_path):
    """Return the number of pages in the given PDF."""
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            page_count = len(pdf.pages)
            print(f"Number of pages in the PDF: {page_count}")
            return page_count
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read PDF: {str(e)}")
        return 0

def convert_pdf_to_image(output_dir, page_num, pdf_path, progress_var):
    try:
        images = convert_from_path(pdf_path, first_page=page_num + 1, last_page=page_num + 1)
        output_file_path = os.path.join(output_dir, f'{os.path.basename(pdf_path).split(".")[0]}_page_{page_num + 1}.png')
        images[0].save(output_file_path, 'PNG')
        messagebox.showinfo("Info", f"Conversion of page {page_num + 1} complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion error: {str(e)}")
    finally:
        progress_var.set(100)

def select_pdf():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        pdf_file_path.set(file_path)
        selected_file_label.config(text=os.path.basename(file_path))

def select_output_directory():
    global output_dir
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_dir_label.config(text=output_dir)

def start_conversion():
    if not pdf_file_path.get():
        messagebox.showerror("Error", "No PDF file provided!")
        return

    try:
        page_num = int(page_number_entry.get()) - 1
        print(f"Page to convert: {page_num + 1}")
    except ValueError:
        messagebox.showerror("Error", "Invalid page number!")
        return

    path = pdf_file_path.get()
    print(f"Path to convert: {path}")

    total_pages = get_pdf_page_count(path)
    if total_pages > 0 and 0 <= page_num < total_pages:
        progress_var.set(0)
        conversion_thread = threading.Thread(target=convert_pdf_to_image, args=(output_dir, page_num, path, progress_var))
        conversion_thread.start()
    else:
        messagebox.showerror("Error", f"Page number out of range! PDF has {total_pages} pages.")

root = tk.Tk()
root.title("PDF to PNG Converter")

pdf_file_path = tk.StringVar()
output_dir = ""
progress_var = tk.IntVar()

select_pdf_button = tk.Button(root, text="Select PDF", command=select_pdf)
select_pdf_button.pack(pady=10)

selected_file_label = tk.Label(root, text="", font=("Arial", 10))
selected_file_label.pack(pady=5)

page_number_label = tk.Label(root, text="Enter Page Number:", font=("Arial", 10))
page_number_label.pack(pady=5)
page_number_entry = tk.Entry(root)
page_number_entry.pack(pady=5)

select_output_dir_button = tk.Button(root, text="Select Output Directory", command=select_output_directory)
select_output_dir_button.pack(pady=10)

output_dir_label = tk.Label(root, text="", font=("Arial", 10))
output_dir_label.pack(pady=5)

convert_button = tk.Button(root, text="Convert", command=start_conversion)
convert_button.pack(pady=20)

root.geometry("600x400")
root.mainloop()
