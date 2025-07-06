import fitz

docs = fitz.open("docs\dl-curriculum.pdf")
page = docs[0].get_text()
print(page)