import pyqrcode
from pyqrcode import QRCode
from PIL import Image as pil_image
from exif import Image as ex_image
import uuid

import constant

def Png_Jpg_Convert(file_name):
    jpg_qr = pil_image.open(f"{constant.PNG_PATH}/{file_name}.png")
    jpg_qr.save(f"{constant.JPG_PATH}/{file_name}.jpg", scale = constant.IMG_RESOLUTION)

def Qr_Generation():
    file_name = str(uuid.uuid4())
    site = constant.URL + str(uuid.uuid4().hex)
    url = pyqrcode.create(site)
    r = url.png(f"{constant.PNG_PATH}/{file_name}.png", scale = constant.IMG_RESOLUTION)
    Png_Jpg_Convert(file_name)
    return file_name

def Write_to_Metadata(file_name, Encrypted_message):
    folder_path = constant.JPG_PATH
    img_path = f"{folder_path}/{file_name}.jpg"

    with open(img_path, 'r+b') as img_file:
        img = ex_image(img_file)
        img.make = Encrypted_message
    with open(img_path, 'r+b') as img_file:
        img_file.write(img.get_file()) 

def Read_to_MetaData(file_name):
    with open(file_name, 'rb') as img_file:
        img = ex_image(img_file)
        em = img.get(constant.META_FIELD)
    return em