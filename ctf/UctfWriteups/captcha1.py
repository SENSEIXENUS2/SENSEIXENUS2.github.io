#! /usr/bin/env python
import requests
import base64
import pytesseract
import os
os.system("mkdir special")
class extractor:
      @staticmethod
      def textextractor(text):
          unimage = text.split('base64,')[1].split('"')[0]
          return unimage
class solver(extractor):
      def __init__(self):
          self.url = requests.Session()
          self.main = self.url.get("https://captcha1.uctf.ir").content.decode()
          self.counter = 0
      def returnImage(self):
        return self.main
      def image(self,text: bytes,imagenum):
          os.system(f"touch special/{imagenum}.jpg")
          dec = base64.b64decode(text)
          image = open(f"special/{imagenum}.jpg","wb")
          image.write(dec)
          image.close()
          path = f"special/{imagenum}.jpg"
          x = pytesseract.image_to_string(path)
          x = x.replace("\n","")
          if "." in x:
              x = x.replace(".","")
          elif "uctf{" in x:
              print(x.content)
              exit()
          print(f"[+]Captcha's answer is {x}")
          return x
      def submit(self,text):
          text = {"captcha":f"{text}"}
          x = self.url.post("https://captcha1.uctf.ir",data=text).content.decode()
          if "that ain't right" in x:
              print("[+]Error")
          elif "UCTF{" in x:
              possible_flag= x
              flag_text=possible_flag.split("UCTF{")[1].split("}")[0]
              print(f"The flag is UCTF{{{flag_text}}}")
              exit()
          else:
              print(f"[+]Successfully submitted,Currently at {self.counter}")
              self.counter += 1
          return super().textextractor(x)
if __name__ == "__main__":
   start = solver()
   global text
   text = start.returnImage()
   extract = extractor()
   text = extract.textextractor(text)
   for i in range(1500):
       image = start.image(text,i)
       text = start.submit(image)
