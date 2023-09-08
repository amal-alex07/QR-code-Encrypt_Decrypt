# driver.py
# Author: Amal Alex
# Date: September 8, 2023
# Description: This driver.py file demonstrates the Key generation and key validation process.

import uuid
import constant
from code import Encrypt, Decrypt
from image import Qr_Generation, Write_to_Metadata, Read_to_MetaData
from storage import Write_to_Database, Read_from_Database, Write_key_Status

# msg contains the confidential data need to be encrypt 
msg = "Hello Mr.Hacker, How are you?"
# key is main actor in this process, helps to encrypt the data, also need the same key at the decrypt time 
key = "hack123456789"

user_name = "hacker"
file_uuid = str(uuid.uuid4())

u = Encrypt(user_name, key, constant.PADDING_SIZE)
f = Encrypt(file_uuid, key, constant.PADDING_SIZE)
c = Encrypt(msg, key)

file_name = Qr_Generation()
Write_to_Metadata(file_name, u+f+c)
Write_to_Database(user_name, file_uuid)

em = Read_to_MetaData(file_name)

try:
    key = input("Enter your key: ")
    ud = Decrypt(em[:constant.NAME_INDEXING] ,key)
    fd = Decrypt(em[constant.NAME_INDEXING:constant.MSG_INDEXING], key)
    result = Read_from_Database(ud, fd)
    if result[0]:
        cd = Decrypt(em[constant.MSG_INDEXING:], key)
        Write_key_Status(ud, fd)
    else:
        print("Key Expired.!")
except UnicodeDecodeError as e:
    print("Invalid Key")


print(ud)
print(fd)
print(cd)
