#! /usr/bin/env python
from Crypto.Util.number import *
import libnum
n1 = 92654857070767571890017042106637703986449117869087364338047922606069735162919
n2 = 98572474388371800971130449337009030864118807314878868777502700832091542642841
n3 = 51501476121983355743052534942567218556170618226963749616587274414221577824191
c1=74597365847504917912916866838569123286395165031450770943853702985527537374325
c2=7392488009685177703766329111985085924328495872306844961776805115046085005730
c3=21070202880950860480001393449893080177749578386435659153510821967923393222435
mod=[n1,n2,n3]
rem=[c1,c2,c3]
res = libnum.solve_crt(rem,mod)
val = libnum.nroot(res,3)
msg = long_to_bytes(val)
print(msg.decode())
