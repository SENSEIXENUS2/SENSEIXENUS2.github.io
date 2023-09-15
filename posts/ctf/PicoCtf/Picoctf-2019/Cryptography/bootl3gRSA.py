#! /usr/bin/env python3
import owiener
from Crypto.Util.number import *
n = 97472804262328485715155491240575299811876899741142060453704584942550929214641250242328566496104782431785416351678437007357087171225126706652980489508751380583151395164555506795779085367697409984974146798634432871269019691150290839061837453348894940259531613679111950047922040304461105515733688007665026783133
e = 8540043671121506400604587190493665738739905066048761937915554980242114157658575444274999295369541796592945369658934423245561965564103903895530982052264374507592992073272694919872403635039185038386461040449435143995023544852821672885279095253112409229090164972310979943244657166139499675284437248179818246913
c = 19306980646063136616550774493801782391126082674648009791344059997482696983809554744665805428272973445424887086897604593232330168912227481360901942814420032058977947098671849378885190980928750027001039447254329292975196963668587916237625942323257367113783498161922195997285485956580829672033442884820451426394
#Finding the decryption key(d)
d = owiener.attack(e,n)
print(d)
flag = pow(c,d,n)
flag = long_to_bytes(flag).decode()
print(flag)

