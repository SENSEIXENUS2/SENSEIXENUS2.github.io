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

