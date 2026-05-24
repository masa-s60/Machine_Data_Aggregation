from pathlib import Path
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

folder = Path(r"C:\Users\fsmn2\OneDrive\画像\スクリーンショット")

files = list(folder.glob("*.png"))

print(files)

img = Image.open(files[0])

print(img)

total_rotation_rect = img.crop((650, 465, 715, 730))

total_rotation_rect = img.crop((650, 465, 715, 730))


total_rotation_rect.show()

text = pytesseract.image_to_string(total_rotation_rect)

print(text)