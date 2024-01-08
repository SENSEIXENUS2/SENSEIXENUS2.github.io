* * *
  ### Ignite
  Lab: THM
* * *

- Rustscan's result

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6e80eeec-2165-44af-af13-121347255ff9)

- The webpage reveals the FUEL content management system 1.4.0

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c477767f-6e77-4447-92a4-eb99dcde4306)

- Exploit database has an exploit for FUELCMS1.4.1,<a href="https://www.exploit-db.com/exploits/50477">Link to exploit</a>

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e986eea2-b748-4a67-a7f9-b1c236942e3d)

- I found an exploit on github which allows us to pop a reverse shell or a shell.<a href="https://github.com/AssassinUKG/fuleCMS">Exploit</a>

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/96d08669-3778-4c54-83f0-d67a8e3296b6)

### FOOTHOLD
- We have gained access to the server

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5343adeb-8b43-4b71-90ef-5bd461433992)

### PRIVESC

- The server runs a pkexec binary that can be used for privilege escalation(pkexec0.105).<a href="https://github.com/arthepsy/CVE-2021-4034">Link to exploit</a>

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/28b5d43b-b071-4b5e-9ae4-e1efae95bd2b)

- Receive the exploit with wget via python http.server and compile the code with gcc.Finally, we have gained root access.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/182ac08d-e6fe-4263-a2ac-320ffe2ad4a0)

