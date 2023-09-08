#! /usr/bin/env python3
import sys
class isHex:
      @staticmethod
      def checkHex(text: str) -> bool:
          try:
              t = int(text,16)
              return True
          except ValueError:
                 return False
class xor(isHex):
    def __init__(self,encText: str):
        if super().checkHex(encText) is True:
           self.encText= bytes.fromhex(encText)
        else:
            print("[+]The bytes is not in hex,provide the xor string in hex")
            exit()
    def singleByteBrute(self,flag_prefix: str):
        enc_text = self.encText.decode("utf-8")
        for key in range(256):
            text = ''.join(chr(ord(char) ^ key) for char in enc_text)
            print(f"[+] Trying Key{key}:Result:{text}")
            if f"{flag_prefix}" in text:
               print(f"[+]The flag is {text} and the key is {key}")
               exit()
            else:
                pass
if __name__ == '__main__':
   solve = xor("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
   solve.singleByteBrute("crypto{")


