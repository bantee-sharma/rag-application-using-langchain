from PIL import Image
from rembg import remove

input_path = "IMG_20250329_1432297.jpg"
output_img = ""

input = Image.open(input_path)
output = remove(input)
output.save(output_img)