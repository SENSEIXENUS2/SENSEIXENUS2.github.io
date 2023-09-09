#! /usr/bin/env python
import base64
enc = "dXRmbGFne2NvdmVyZWRfYWxsXzY0X2Jhc2VzfQo="
dec = base64.b64decode(enc)
print(dec.decode())
