import fitz

file = fitz.open("docs/dl-curriculum.pdf")


for page_no in range(len(file)):
    page = file.load_page(page_no)
    text = page.get_text()
    print(f"Page no: {page_no} \n\ {"-"*30} \n\ {text}")