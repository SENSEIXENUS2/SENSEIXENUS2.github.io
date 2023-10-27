   I played questcon ctf with my friends so I decided to make a writeup on the challenges.I solved different challeneges ranging from web,misc,
 crypto and steg0.

 ### Challenge 1
   Challenge type: crypto
  ![2023-10-27_21-20](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0cfec003-7559-4e12-9ed5-1e380baddb8f)

- After opening the file on linux cli,I noticed that it was RSA and n,e,c was given.I wrote a script for it 

      ┌──(sensei㉿kali)-[~/Downloads]
      └─$ cat Cryptographic_Treasure.txt
      N = 882564595536224140639625987659416029426239230804614613279163
      E = 65537
      C = 164269225538436495685306542268826436068505673594249194166792

- I ran the script and got this. <a href="">Link to the script</a>

       ┌──(sensei㉿kali)-[~/Documents/scripts]
       └─$ ./treasure.py
        QUESTCON{1_HaT3_RS1}
