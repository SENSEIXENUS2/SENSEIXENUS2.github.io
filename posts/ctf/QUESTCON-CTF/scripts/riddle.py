#! /usr/bin/env python3
import base64
from pwn import *
#key is 3
key = chr(3).encode()
ct = b'VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>'
text: bytes = xor(ct,key)
flag = base64.b64decode(text).decode()
print(flag)
