from PyPDF2 import PdfReader

myPDF = "document2.pdf"

full_text = ""

with open(myPDF, "rb") as input_pdf:
    pdf_reader = PdfReader(input_pdf)
    num_pages = len(pdf_reader.pages)

    for page_number in range(num_pages):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        print(f"Texto da página {page_number + 1}:\n{text}\n")
        full_text += text + "\n"
