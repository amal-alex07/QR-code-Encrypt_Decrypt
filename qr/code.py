# code.py
# Author: Amal Alex
# Date: September 7, 2023
# Description: This code.py demonstrates the Encryption and Decryption functions.

from Crypto.Cipher import Blowfish
from Crypto import Random
import base64

import constant

# padding function 
def Do_Padding(s, block_size):
    padding = constant.PADDING
    p = lambda s: s+ (block_size - len(s) % block_size) * padding
    return p(s)

# Encrypt function
def Encrypt(msg, key, block_size=8):
    key = str.encode(key)
    iv = Random.new().read(Blowfish.block_size)
    msg = Do_Padding(msg, block_size)
    c = Blowfish.new(key, Blowfish.MODE_CBC,iv)
    Encrypted_message = iv + c.encrypt(msg.encode('ascii'))
    return base64.b64encode(Encrypted_message).decode()

# Decrypt function
def Decrypt(Encrypted_message, key):
    key = str.encode(key)
    Encrypted_message = str.encode(Encrypted_message)
    block_size = Blowfish.block_size
    Encrypted_message_ = base64.b64decode(Encrypted_message) [block_size:]
    iv = base64.b64decode(Encrypted_message) [:block_size]
    d = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    return d.decrypt(Encrypted_message_).decode('ascii').rstrip(constant.PADDING)