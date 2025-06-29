import fitz

docs = fitz.open("docs/dl-curriculum.pdf")
print(len(docs))