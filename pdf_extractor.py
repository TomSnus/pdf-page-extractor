import os
import PyPDF2
from zipfile import ZipFile

def extract_pages(pdf_path, page_numbers):
    pdf_writer = PyPDF2.PdfWriter()

    try:
        pdf_reader = PyPDF2.PdfReader(pdf_path)
        print(f"Verarbeite '{pdf_path}' mit insgesamt {len(pdf_reader.pages)} Seiten.")
        for page_num in page_numbers:
            pdf_writer.add_page(pdf_reader.pages[page_num - 1])
    except IndexError:
        print(f"Fehler: Eine der spezifizierten Seiten ist außerhalb des Bereichs des Dokuments in '{pdf_path}'.")
    except Exception as e:
        print(f"Unbekannter Fehler beim Verarbeiten von '{pdf_path}': {e}")

    return pdf_writer

def save_extracted_pages_to_zip(input_directory, page_numbers, output_zip_path):
    pdf_files = [f for f in os.listdir(input_directory) if f.lower().endswith('.pdf')]
    extracted_files = []

    with ZipFile(output_zip_path, 'w') as zip_output:
        for pdf_file in pdf_files:
            pdf_path = os.path.join(input_directory, pdf_file)
            pdf_writer = extract_pages(pdf_path, page_numbers)

            extracted_pdf_path = os.path.join(input_directory, f"3TTX_{pdf_file}")
            with open(extracted_pdf_path, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)

            zip_output.write(extracted_pdf_path, os.path.basename(extracted_pdf_path))
            extracted_files.append(extracted_pdf_path)

    # Cleanup: Remove the individual extracted PDF files after zipping
    for extracted_file in extracted_files:
        os.remove(extracted_file)

    print(f"All extracted pages are saved and zipped in '{output_zip_path}'.")

# Input directory containing all PDF files
input_directory = r'<path>'

# Page numbers to extract (starting from 1)
pages_to_extract = [2, 3]

# Output ZIP file path
output_zip_file = r'<path>'

# Run the script
save_extracted_pages_to_zip(input_directory, pages_to_extract, output_zip_file)
