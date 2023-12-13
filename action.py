import os
from PyPDF2 import PdfWriter, PdfReader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(BASE_DIR, "PDF_folder")
output_folder = os.path.join(BASE_DIR, "Outputs")

if not os.path.isdir(input_folder):
    os.mkdir(input_folder)
if not os.path.isdir(output_folder):
    os.mkdir(output_folder)

file_names_with_ext = os.listdir(input_folder)

for file in file_names_with_ext:
    # read pdf and get first page
    print(f"Processing: {file}")
    file_full_path = os.path.join(input_folder, file)
    target_file = open(file_full_path, mode='rb')
    pdf = PdfReader(target_file)
    first_page = pdf.pages[0]
    output_pdf = PdfWriter()
    output_pdf.add_page(first_page)
    output_pdf.write(os.path.join(output_folder, file))
    target_file.close()
    print(f"{file} ---- Done")
   