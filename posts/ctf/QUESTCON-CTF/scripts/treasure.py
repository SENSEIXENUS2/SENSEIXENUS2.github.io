#! /usr/bin/env python
from Crypto.Util.number import *

#N,e,c
n: int = 882564595536224140639625987659416029426239230804614613279163
e: int = 65537
c: int = 164269225538436495685306542268826436068505673594249194166792
#Prime factors of n(Via factordb.com)
p: int = 857504083339712752489993810777
q: int = 1029224947942998075080348647219
#Finding phi
phi: int = (p-1)*(q-1)
#Private key
d: int = inverse(e,phi)
flag: str = long_to_bytes(pow(c,d,n)).decode()
print(flag)
