#! /usr/bin/env python
import json
from pwn import *
import base64
import codecs
from Crypto.Util.number import *
'''Solving cryptohack network attacks challenges with Object Oriented Programming'''
#creating a class for decoding it
class solver:
      def base64(self,enctext):
          print(f"[+]Decoding Base64text:{enctext}")
          dectext = base64.b64decode(enctext)
          return dectext.decode()
      def hex(self,enctext):
          print(f"[+]Decoding Hextext:{enctext}")
          dectext = bytes.fromhex(enctext)
          return dectext.decode()
      def rot13(self,enctext):
          print(f"[+]Decoding ROT13text:{enctext}")
          dectext = codecs.decode(enctext,"rot13")
          return dectext
      def bigint(self,enctext):
          print(f"[+]Decoding Biginttext:{enctext}")        
          enctext = str(enctext)
          enctext = int(enctext,16)
          dectext = long_to_bytes(int(enctext))
          return dectext.decode()
      def utf8(self,enctext):
          print(f"[+]Decoding utf8text:{enctext}")
          dectext = ''.join(chr(x) for x in enctext)
          return dectext
class connector():
    def __init__(self,addr: str,port: int):
        self.addr = addr
        self.port = port
        print(f"[+]Connecting to {self.addr}:{self.port}")
        self.connection = remote(self.addr,self.port)
    def receive(self):
        c = self.connection
        received = c.recv()
        if b"crypto{" not in received:
            received = json.loads(received)
#checking for the flag        
        else:
            received = received.decode()
            received = json.loads(received)
            received = received['flag']
            received = received.split("crypto{")[1].split("}")[0]
            received = f"crypto{{{received}}}"
            print(received)
            exit()
        return received
    def send(self,text):
        print(f"[+]Sending Decodedtext:{text}")
        c = self.connection
        sending = json.dumps(text)
        sending = sending.encode()
        c.send(sending)
if __name__ == "__main__":
   word = connector("socket.cryptohack.org",13377)
   solver = solver()
   for i in range(0,101):
       x = word.receive()
       typ = x["type"]
       encoded = x["encoded"]
       print(f"[+]Decoding for {i}:{encoded}")
       if typ == "base64":
          text  = solver.base64(encoded)
       elif typ == "hex":
            text = solver.hex(encoded)
       elif typ == "rot13":
           text = solver.rot13(encoded)
       elif typ == "bigint":
           text = solver.bigint(encoded)
       elif typ == "utf-8":
           text = solver.utf8(encoded)
       decoded = {"decoded": text}
       word.send(decoded)

