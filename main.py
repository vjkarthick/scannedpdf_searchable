

import subprocess


def convert_scanned_pdf_to_searchable_pdf(input_pdf_path, output_pdf_path):
    try:
        subprocess.run(
            ['ocrmypdf', '--force-ocr', input_pdf_path, output_pdf_path],
            check=True,
            text=True,  # Capture stdout as text
            input='Y\n'  # Provide the input "Y" followed by a newline as a string
        )
        print("Conversion successful!")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


input_pdf_path = 'C:/Users/Admin/Downloads/c4611_sample_explain (1).pdf'
output_pdf_path = 'D:/scanned/output_searchable.pdf'

convert_scanned_pdf_to_searchable_pdf(input_pdf_path, output_pdf_path)
