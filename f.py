import fitz

file = fitz.open("docs\PA - Consolidated lecture notes.pdf")

for page_num in range(len(file)):
    page = file.load_page(page_num)
    text = page.get_text()
    print(f"Page No.-{page_num+1}\n {"_"*30} \n {text}")
