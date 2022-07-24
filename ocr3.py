import pytesseract
from PIL import Image
import re
from pdf2image import convert_from_path


def parser(left, top, right, bottom, parse_name):
    images = convert_from_path('/Users/yunusemre/Desktop/yerlesim.pdf', 500)
    for img_no in range(len(images)):
        images[img_no].save('page' + str(img_no) + '.jpg', 'JPEG')
    page = 'page' + str(img_no) + '.jpg'

    img = Image.open(page)
    image = img.crop((left, top, right, bottom))
    image.save(parse_name + '.jpg')
    parse = pytesseract.image_to_string(Image.open(parse_name + '.jpg'), lang='tur')
    for parse in list(parse.split("\r")):
        parse = re.sub(r'\n', ' ', parse)
    return parse


citizen_id = parser(1220, 1700, 3000, 1800, "citizen_id")
name = parser(1220, 1800, 3000, 1900, "name")
surname = parser(1220, 1900, 3000, 2020, "surname")
is_domestic = parser(1000, 2200, 1500, 2500, "is_domestic")
result = True if is_domestic == 'Yurtiçi ' else False
address_no = parser(1500, 2200, 1990, 2500, "address_no")
open_address = parser(1970, 2000, 3700, 2700, "open_address")
print(citizen_id)
print(name)
print(surname)
print(result)
print(address_no)
print(open_address)