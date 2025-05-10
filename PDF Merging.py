from pypdf import PdfWriter, PdfReader
import os

merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]

# for pdf in files:
#     merger.append(pdf)

for pdf in files:
    reader = PdfReader(pdf)
    for page in reader.pages:
        if "/Annots" in page:  # Remove all annotations
            del page["/Annots"]
        merger.add_page(page)

merger.write("merged-pdf.pdf")
merger.close()

# code to check if a pdf has any issue 

from pypdf import PdfReader
import os

files = [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
    try:
        reader = PdfReader(pdf)
        print(f"{pdf} opened successfully!")
    except Exception as e:
        print(f"Error in {pdf}: {e}")
