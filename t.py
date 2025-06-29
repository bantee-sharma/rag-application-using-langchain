import fitz

docs = fitz.open("docs/dl-curriculum.pdf")
d = docs[1].get_text()
print(d)
# for page_no in docs:
#     page = 
#     print(page)