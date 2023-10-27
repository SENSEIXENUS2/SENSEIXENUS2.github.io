### QUESTON-CTF writeup

   I played questcon ctf with a friend so I decided to make a writeup on the challenges.I solved different challeneges ranging from web,misc crypto to steg0.

 ### Challenge 1
   Challenge type: crypto
  
  ![2023-10-27_21-20](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0cfec003-7559-4e12-9ed5-1e380baddb8f)

- After opening the file on linux cli,I noticed that it was RSA and n,e,c was given.I wrote a script for it 

      ┌──(sensei㉿kali)-[~/Downloads]
      └─$ cat Cryptographic_Treasure.txt
      N = 882564595536224140639625987659416029426239230804614613279163
      E = 65537
      C = 164269225538436495685306542268826436068505673594249194166792

- I ran the script and got this. <a href="https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/QUESTCON-CTF/scripts/treasure.py">Link to the script</a>

       ┌──(sensei㉿kali)-[~/Documents/scripts]
       └─$ ./treasure.py
        QUESTCON{1_HaT3_RS1}
  
### Challenge 2
 Challenge type: crypto
 
 ![2023-10-27_21-36](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4e5c49d2-5ab5-43fe-ad3a-8160e2e2eb4e)

- At first,I auto solved with cyber-chef but I decided to make script on the challenge and also find out how it was solved.

   ![2023-10-27_21-39](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e2ad7e6d-fe1e-46f2-94de-cc8d922f9091)

- I noticed that it was solved with Xor,I tried the single brute technique with python(pwntoools).I noticed that xoring with '3' produces a base64 encoded text.
   
      >>> x = b'VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>'
      >>> for i in range(256):
      ...     print(f"Key:{i}-{xor(x,i)}")
      ... 
      Key:0-b'VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>'
      Key:1-b'WTTDW3PFV275PFO2XD;LO07dTFLq`D;M`3;WLEuxa12?'
      Key:2-b'TWWGT0SEU146SEL1[G8OL34gWEOrcG8Nc08TOFv{b21<'
      Key:3-b'UVVFU1RDT057RDM0ZF9NM25fVDNsbF9Ob19UNGwzc30='

- I wrote a script to autosolve it.

       #! /usr/bin/env python3
       import base64
       from pwn import *
       #key is 3
       ct = b'VUUEV2QGW364QGN3YE:MN16eUGMpaE:La2:VMDty`03>'
       text: bytes = xor(ct,key)
       flag = base64.b64decode(text).decode()
       print(flag)

- And I got this the flag,here is the link to the <a href="https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/QUESTCON-CTF/scripts/riddle.py">script</a>

        ┌──(sensei㉿kali)-[~/Documents/scripts]
        └─$ ./riddle.py
         QUESTCON{D34d_M3n_T3ll_No_T4l3s}
  
  
