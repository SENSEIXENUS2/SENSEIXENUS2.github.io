#! /usr/bin/env python
from Crypto.Util.number import *
from sympy import *
flag = ''
#1
n1 = 1798468255372432132951694743055409613585918
e1 = 65537
c1 = 1515010050704102329460092803733159335563363
p = 2
q = 899234127686216066475847371527704806792959
phi = (p-1)*(q-1)
d = inverse(e1,phi)
msg = pow(c1,d,n1)
msg = long_to_bytes(msg)
msg = msg.decode()
flag += msg
#2
n2 = 25081679729270500375165403529197044453
e2 = 65537
c2 = 23332664177202658872648660306097124315
#finding phi Multi factors 
p = 13151
q = 24923
a = 32693
b = 54493
c = 66463
d = 76847
e = 89069
f = 94421
phi = (p-1)*(q-1)*(a-1)*(b-1)*(c-1)*(d-1)*(e-1)*(f-1)
d = inverse(e2,phi)
msg = pow(c2,d,n2)
msg = long_to_bytes(msg)
msg = msg.decode()
flag += msg
#3
n2 = 25195908475657893494027183240048398571429282126204032027777137836043662020707595556264018525880784406918290641249515082189298559149176184502808489120072844992687392807287776735971418347270261896375014971824691165077613379859095700097330459748808428401797429100642458691817195118746121515172654632282216869987549182422433637259085141865462043576798423387184774447920739934236584823824281198163815010674810451660377306056201619676256133844143603833904414952634432190114657544454178424020924616515723350778707749817125772467962926386356373289912154831438167899885040445364023527381951378636564391212010397122822120720357
e3 = 3
c3 = 359272128281507565669
msg = cbrt(c3)
msg = long_to_bytes(msg)
msg = msg.decode()
flag += msg
print(flag)
