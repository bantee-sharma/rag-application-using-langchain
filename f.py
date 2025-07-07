import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io
import os

docs = fitz.open("docs\PA - Consolidated lecture notes.pdf")

for page_no in range(len(docs)):
    page = docs.load_page(page_no)
    text = page.get_text()

    # print(f"page_no.-{page_no} \n {"-"*30} \n {text}")
    image_list = page.get_images(full=True)
    for image_index,img in enumerate(image_list):
        xref = img[0]
        base_image = docs.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]


        # Convert to PIL Image
        image = Image.open(io.BytesIO(image_bytes))

        # OCR: extract text from the image
        ocr_text = pytesseract.image_to_string(image)

        print(f"\n🖼️ Image {img_index + 1} OCR Text:")
        print(ocr_text.strip())