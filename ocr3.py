from random import randrange
from PIL import Image, ImageFile
from pdf2image import convert_from_path
import pytesseract
import re
from gtts import gTTS
import os
import mysql.connector


def parse_document(filename):
    image_name = randrange(0, 100000)
    images = convert_from_path(filename, 500)
    img_no = len(images) - 1
    page = str(image_name) + '.jpg'
    images[img_no].save(page, 'JPEG')
    with Image.open(page) as image:
        parse = pytesseract.image_to_string(image.crop(), lang='tur')
    for parse in list(parse.split("\r")):
        parse = re.sub(r'\n', '', parse)
        parse = re.sub(r'\f', '', parse)
    os.remove(page)
    myobj = gTTS(text=parse, lang='tr', slow=False)

    myobj.save("/Users/yunusemre/Desktop/welcome2.mp3")

    os.system("/Users/yunusemre/Desktop/welcome2.mp3")
    return parse


parse_document("/Users/yunusemre/Desktop/sis.pdf")
