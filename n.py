import fitz

doc = fitz.open("docs\dl-curriculum.pdf")


for page_no in range(len(doc)):
    page = doc(page_no)
    text = page.get_text()
    print(text)