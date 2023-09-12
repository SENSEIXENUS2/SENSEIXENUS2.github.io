#! /usr/bin/env python
from pwn import *
old_key = "crypto{"
enc_text = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
partial_key = xor(enc_text[:len(old_key)],old_key) + b"y"
key = len(enc_text) * partial_key
complete_key = key[:len(enc_text)]
print("The flag is ",xor(enc_text,complete_key).decode())
