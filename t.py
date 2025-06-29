import fitz

docs = fitz.open("docs/dl-curriculum.pdf")

for page_no in range(len(docs)):
    page = docs.load_page(page_no)
    text = page.get_text()
    print(f"Page No.{page_no}\n{"---"*30}\n{text}")

