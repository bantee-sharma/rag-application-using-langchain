import fitz

docs = fitz.open("docs\PA - Consolidated lecture notes.pdf")

for page_no in range(len(docs)):
    page = docs.load_page(page_no)
    text = page.get_text()

    # print(f"page_no.-{page_no} \n {"-"*30} \n {text}")
    image_list = page.get_images(full=True)
    print(image_list)