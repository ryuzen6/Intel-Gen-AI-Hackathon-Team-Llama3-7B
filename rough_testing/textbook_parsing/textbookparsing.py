import re
from pdfminer.high_level import extract_pages, extract_text
import fitz #PyMuPDF
import PIL.Image #pillow
import io
import tabula
import sys

sys.stdout.reconfigure(encoding='utf-8')

#Extract textbook text from Textbook
def extractTextbookText(pdf=""):
    text = extract_text(pdf)
    return text

#Extract images from a pdf
pdf = fitz.open("rough_testing/textbook_parsing/NCERT_11.pdf")
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img.save(open(f"rough_testing/textbook_parsing/textbook_images/image{counter}.{extension}","wb"))
        counter +=1