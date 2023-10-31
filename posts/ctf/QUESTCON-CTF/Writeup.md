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
   ![2023-10-31_18-18](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f99508ef-73c4-4982-b271-81a8cd6debcd
   
- The challenge contained an image
  ![another_mystery](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/856ebc99-4da2-46c9-8a73-f532350e598f)

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

![2023-10-31_18-30](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1037554c-c807-43dc-a821-633a62636d85)
### Challenge 4:
  
   Challenge description: Web
   ![2023-10-31_18-30](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6eaa602f-100e-4d5d-9ee4-1be1f6984084)

- The main aim of the challenge is to find Captain Jack sparrow's hidden treasure.I used curl to solve the challenge.

- The first hurdle as to access the browser with a pirate browser

  ![2023-10-31_18-34](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6aa308d1-9722-47a0-9812-7f424a8013f3)

- I bypassed it with the user-agent header because the user-agent header contains the browser information.

      curl https://questcon-pirate-treasure.chals.io/ -H "User-agent: pirate"

- The next hurdle is to be from the ship Black Perl.

  ![2023-10-31_18-39](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/aba4135c-e0f0-449d-a87b-f9fbdc88dd2f)

- I also passed this hurdle with the Referer header because it indicates the site that directed the user to tht site.

        
  -
