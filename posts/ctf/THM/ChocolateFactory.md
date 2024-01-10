* * *
  ### LAB: TryHackMe
  ### Chocolate Factory
* * *

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9e33c33b-e6cf-48ca-95ae-54fdad647e19)


### Enumeration
- Rustscan reveals a scary amount of ports but I'll wait for NMAP's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f1aea04c-eaad-4ceb-baaa-e2cfe649e670)

   
- Nmap reveals the same amount of ports
  
  
- The Apache web server provides a login page

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/31e53968-d9c4-4479-ab61-4b0b114dbb8c)

- I started with FTP(port 21),it has anonymous login (username: anonynous and pasword: password) which contains an image file(.jpg)

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bf5a580e-31f5-43dd-82ba-a9016659efbc)

- I later discovered the file to be steganography image after cracking it with stegseek,download files with FTP with ( get <filename>)
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/07a72bf0-56c5-41aa-8416-2d5723f3d6b0)

- The file contains base64 encoded contents which I decoded with the base64 linux utility

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/39ed3966-0ae7-4ff7-897b-baa71fb76df2)

- The file also contains Charlie's hash

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b0330281-e8a3-4a84-b0c6-6465f6aa0147)

- I cracked the hash with John the Ripper

     ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f02f3b3e-a5f0-4c32-9952-9f9b66c42c1d)

- The password is Charlie's login detail for the webpage and the page reveals a page to execute commands which we can use to get rce

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/50057ce7-e2c8-4cb1-a1dc-e119cc21706d)

- Now we have a stabilized shell

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/630d77db-10a8-41ec-a1c1-91c45d28c9bb)

### Privesc

- Charlie's home directory contains a private ssh key file

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6bf3f47c-a9d0-4232-b570-b4512f27a431)

- I started a python http server on the target machine to copy the key to the attack machine

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/54f94793-41d8-4c01-89f0-9597a1f62c31)

- SSH access with Charlie's account

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/688cb033-69c5-42a5-9cf6-618bff15515b)

- Sudo -l indicates that we can use sudo vi without a password which we can use to escalate to root

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ed23fb18-8dfb-4363-b11b-31c94109dbd8)

- We can escalate privileges with this

      sudo /usr/bin/vi
      :!/bin/bash

- Root access

     ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cb641267-21f8-4d42-8429-3beaa6625a9c)

### Root Flag

- The root account contains a Fernet encryption code which requires a key

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/36781c37-e347-4ef8-83ae-a4fdf7a469f5)

- The key is in the key_rev file in /var/www/html directory

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/85b2a211-8ff7-4e4f-8ad9-647697d47fc3)

- Root flag

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cf726829-d5c5-4844-a7d4-f6b9dfd9075c)

   
