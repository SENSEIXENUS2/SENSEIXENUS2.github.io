#! /usr/bin/env python
from PIL import Image
class imageLoad:
      def __init__(self):
          self.image1 = Image.open("lemur.png")
          self.image2 = Image.open("flag1.png")
          self.flag = Image.open("flag.png")
          self.image1Pixels = self.image1.load()
          self.image2Pixels = self.image2.load()
          self.flagPixels = self.flag.load()
      def loadImages(self,pos1: int,pos2: int):
          image1pix = self.image1Pixels
          image2pix = self.image2Pixels
          try:
             pix1 = image1pix[pos1,pos2]
             pix2 = image2pix[pos1,pos2]
             return pix1,pix2
          except IndexError:
                return "false","false"
      def xorPixels(self,pixel1: tuple or str,pixel2: tuple or str) -> tuple:
          flag = []
          if pixel1 and pixel2 != "false":
             flag.append(pixel1[0] ^ pixel2[0])
             flag.append(pixel1[1] ^ pixel2[1])
             flag.append(pixel1[2] ^ pixel2[2])
             return tuple(flag)
          else:
              return "skip"
      def submit2Flag(self,rgbVal: tuple,pos1: int,pos2: int):
          if rgbVal != "skip":
             self.flagPixels[pos1,pos2] = rgbVal
             print(f"[+]Added values for {pos1}:{pos2}")
          else:
              pass
      def flagSave(self):
          self.flag.save("newflag.png")
          print("[+]newflag.png Created")
if __name__ == '__main__':
   image = imageLoad()
   for pos1 in range(600):
       print(f"[+]Working on Position:{pos1}")
       for pos2 in range(400):
           (pixel1,pixel2) = image.loadImages(pos1,pos2)
           flagPixel = image.xorPixels(pixel1,pixel2)
           image.submit2Flag(flagPixel,pos1,pos2)
   image.flagSave()
