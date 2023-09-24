#! /usr/bin/env python
from pwn import *
#First Blood
#RepeatingXOR ting
ciphertext = bytes.fromhex('020b57052839720f3a58463c0a1f072b0e5c0617581f6b4405374b5319325047001a4a131f5c041a1e')
known_text = "acdfCTF{"
#getting the key
key2 = xor(ciphertext[:len(known_text)],known_text)
key = key2 * len(ciphertext)
key = key[:len(ciphertext)]
flag = ''.join(chr(i ^ j)for i,j in zip(ciphertext,key))
print(flag)

