### QUESTON-CTF writeup

   I played questcon ctf with a friend so I decided to make a writeup on the challenges.I solved different challenges ranging from web,misc,crypto to steg0.

### Challenge 1:
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
  
### Challenge 2:
 Challenge type: crypto
 
 ![2023-10-27_21-36](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4e5c49d2-5ab5-43fe-ad3a-8160e2e2eb4e)

- At first,I auto solved with cyber-chef but I decided to make script on the challenge and also find out how it was solved.

   ![2023-10-27_21-39](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e2ad7e6d-fe1e-46f2-94de-cc8d922f9091)

- I noticed that it was solved with Xor,I tried the single byte bruteforce xor attack with python(pwntools).I noticed that xoring the ciphertext with '3' produces a base64 encoded text.
   
      >>> from pwn import *
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
  
### Challenge 3:
   Challenge description: misc 
    
   ![2023-10-31_18-11](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ea5c8cca-3d19-4544-ad8f-95fe096e77ae)
- The aim of the challenge was to find the port numbers and use a formula to find the answer.I automated it with python

      #! /usr/bin/env python3
      #Port numbers
      whois = 43
      qotd = 17
      chargen = 19
      xfer = 82
      echo = 7
      nntp = 119
      nsca = 5667
      dce = 135
      #calculation
      print(f"QUESTCON{{{((((whois + qotd) * chargen) - xfer) % echo) * (dce + nntp) * nsca}}}")
- Script result

      ┌──(sensei㉿kali)-[~/Documents/scripts]
      └─$ ./seaofports.py
      QUESTCON{1439418}

### Challenge 4:
 Challenge description: Steganography
   
   ![2023-10-31_18-18](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f99508ef-73c4-4982-b271-81a8cd6debcd)
   
- The challenge contained an image

  ![2023-10-31_18-18](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/856ebc99-4da2-46c9-8a73-f532350e598f)

- I used file linux utility to get the file type.It confirmed that it is a png file.
  ![2023-10-31_18-22](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/599bcde5-06ec-4a45-9c50-d6093d60d42e)

- I decided to try png file steganography technique.I tried stegolsb to check for least significant bit.I used this command

        stegolsb steglsb -r -i another_mystery.png -n 2 -o output.txt
    
- Challenge solved

      ┌──(sensei㉿kali)-[~/Downloads]
      └─$ stegolsb steglsb -r -i another_mystery.png -n 2 -o output.txt
      Files read                     in 0.90s
      30 bytes recovered             in 0.00s
      Output file written            in 0.00s

      ┌──(sensei㉿kali)-[~/Downloads]  
      └─$ cat output.txt
      QUESTCON{P1raT3s_Ar3_M7s!3rY}

### Challenge 4:
  Challenge description: Web
   
   ![2023-10-31_18-30](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6eaa602f-100e-4d5d-9ee4-1be1f6984084)

- The main aim of the challenge is to find Captain Jack sparrow's hidden treasure.I used curl to solve the challenge.

- The first hurdle as to access the browser with a pirate browser

  ![2023-10-31_18-34](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6aa308d1-9722-47a0-9812-7f424a8013f3)

- I bypassed it with the user-agent header because the user-agent header contains the browser information.

      curl https://questcon-pirate-treasure.chals.io/ -H "User-agent: pirate"

- The next hurdle is for the user to be from the ship Black Perl.

  ![2023-10-31_18-39](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/aba4135c-e0f0-449d-a87b-f9fbdc88dd2f)

- I also passed this hurdle with the Referer header because it indicates the site that directed the user to that site.

       curl https://questcon-pirate-treasure.chals.io/ -H "User-agent: pirate" -H "Referer: Black Perl"
- The next hurdle is to identify yourself to get the treasure.I knew it was the cookie header but finding the cookie value  was a bit hard.My teammate Oxvip found it and solved it.

  ![2023-10-31_18-50](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/40c33c89-9f77-4343-bfe7-61cd3ae35620)

- I added the cookie value "user=jack sparrow" and got the flag.

         curl https://questcon-pirate-treasure.chals.io/ -H "User-agent: pirate" -H "Referer: Black Perl" -H "Cookie: user=jack sparrow; expires=Thu, 30-Nov-2023 14:52:47 GMT; Max-Age=2592000; path=/"
         <!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
         <title>Pirate's Treasure Hunt</title>
         <link rel="stylesheet" href="styles.css">
         </head>
         <body>
         <div>QUESTCON{Thr33_k33p_a_s3cr3t_if_2_of_th3m_ar3_dead}</div></body>
         </html>

  ### Challenge 4:
    Challenge description: web

![2023-10-31_19-11](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/37878e98-733e-4eb4-a2f2-f75bc60a4f41)

- The landing page signified "find the flag".

  ![2023-10-31_19-13](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3aa1966c-0b13-48ab-8257-6ad18fb5a0a8)

- I decided to inspect the code and I noticed a string containing ASCII character codes.
  
  ![2023-10-31_19-16](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fe45aa07-60b6-4f81-bb8a-64247e74741e)

- I automated it with python and got the flag

      ┌──(sensei㉿kali)-[~/Downloads]
      └─$ python3
      Python 3.11.5 (main, Aug 29 2023, 15:31:31) [GCC 13.2.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> flagencString = "81 85 69 83 84 67 79 78 123 87 51 66 95 51 88 80 76 48 82 51 82 95 49 83 95 52 87 51 83 48 77 51 125".split(" ")
      >>> flag: str = ''.join(chr(int(char)) for char in flagencString)
      >>> print(flag)
      QUESTCON{W3B_3XPL0R3R_1S_4W3S0M3}

  
### Last Challenge:
   Challenege description: web

![2023-10-31_19-39](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ecb8feb2-46da-437d-9823-daed9008d8e5)

- I checked the website functionality and noticed that it has an id parameter that takes in an hash.

 ![2023-10-31_19-43](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a4bd8ab6-e6d2-427d-bb49-0809113381e0)

- I checked the hash on crackstation and I got a result stating that it is the sha224 value for '2'

![2023-10-31_19-47](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6ba82347-ef9d-4eb6-84f5-e2f0be93c0c5)

- At first I thought the flag will be in one of the pages.Then,I noticed that id '3' was missing. I used hashlib to create an hash

      ┌──(sensei㉿kali)-[~/Documents/scripts]
      └─$ python3
      Python 3.11.5 (main, Aug 29 2023, 15:31:31) [GCC 13.2.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import hashlib
      >>> hash = hashlib.sha224(b'3')
      >>> hash.hexdigest
      <built-in method hexdigest of _hashlib.HASH object at 0x7fe959585fd0>
      >>> hash.hexdigest()
      '4cfc3a1811fe40afa401b25ef7fa0379f1f7c1930a04f8755d678474'
      >>> 
- It granted access to a page but it has a password.I remembered the secret key hint 'Barbossa' and I got the flag.

![2023-10-31_19-55](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/106b7db8-f815-4a74-a9ea-ca7d99606f59)

### Thanks for reading !!!!!!
