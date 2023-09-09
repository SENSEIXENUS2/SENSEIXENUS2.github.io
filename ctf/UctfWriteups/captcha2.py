#! /usr/bin/env python3
import hashlib
import requests
import re
class crackHash():
      @staticmethod
      def crackAnimals(hashx:str):
          wordlistAnimals = ["rabbit","dog","camel","cat","snake","horse","eagle","duck","fox","bear","penguin","mouse"]
          for animal in wordlistAnimals:
              hexhash = hashlib.sha1(animal.encode())
              hexhash = hexhash.digest().hex()
              if hashx.lower() == hexhash:
                 return animal
                 break
      @staticmethod
      def hashCapture(text):
          unhash = re.findall(r"[A-Z0-9]{40}",text)
          return unhash
class solver(crackHash):
      def __init__(self):
          self.url = requests.Session()
          self.main = self.url.get("https://captcha2.uctf.ir/").content.decode()
          self.counter = 0
      def returnmain(self):
          return self.main
      def submit(self,text1: str,text2: str):
          text = f"{text1}-{text2}"
          print(f"[+]Submitting {text}")
          data = {"captcha": f"{text}"}
          x = self.url.post("https://captcha2.uctf.ir/",data = data).content.decode()
          if "that ain't right" in x:
              print("[+]Error")
          elif "more to go!" in x:
              print(f"[+]Successful submitted:Counter:{self.counter}")
              self.counter += 1
          elif "UCTF{" or "uctf{" in x:
              preflag = x.split("UCTF{")[1].split("}")[0]
              flag = f"[+]The flag is UCTF{{{preflag}}}"
              print(flag)
              exit()
          hashes = super().hashCapture(x)
          hash1 = super().crackAnimals(hashes[0])
          hash2 = super().crackAnimals(hashes[1])
          return hash1,hash2
if __name__ == "__main__":
   global hash1,hash2
   solver = solver()
   txt = solver.returnmain()
   text = solver.hashCapture(txt)
   text1 = crackHash.crackAnimals(text[0])
   text2 = crackHash.crackAnimals(text[1])
   for i in range(1,500):
       (text1,text2) = solver.submit(text1,text2)


