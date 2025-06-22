import fitz


doc = fitz.open("docs\PA - Consolidated lecture notes.pdf")

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text = page.get_text()
    print(text)
    