* * *
 ### PHP Include And Post Exploitation
* * *
### Challenge description: 
   This lab focuses on exploiting local file inclusion with directory traversal and also abusing unrestricted file upload in web apps.Directory traversal occurs when an attacker is able to read sensitive file on a webserver and when paths passed to include() php function are not properly sanitized.Unrestricted file upload occurs when an attacker bypassed upload restrictions on a server and upload arbitrary files e.g a web shell as will be shown in this lab
   
   ![2023-12-20_21-56](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/beb66fc2-0a66-42f3-b7b8-c41f14f22d92)

- Use netdiscover to find hosts on the network,host "192.168.184.130" is the lab
  ![2023-12-21_17-48](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8c98401c-fe28-4807-9c0c-fb5e2462dd61)

- Scan for open ports with nmap

      nmap -sv -p- <ip>

  ![2023-12-21_17-53](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6911e126-0e62-4e30-9242-f45b3b644dcd)

- An apache webserver is running on the host,we can fuzz for directories with gobuster

   ![2023-12-21_17-58](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4eead3b9-eed9-4444-bdf3-b88e19034aa5)

- After opening the login page,I noticed this page query "http://192.168.184.130/index.php?page=login" and I tested for local file inclusion.It popped out this error.

   ![2023-12-21_18-02](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d18d08a7-e3d8-4ccd-a388-b4f017cbfef1)

- The server added ".php" to files which made it impossible to read files on the server.I bypassed it with the null byte injection "%00" which excluded the ".php" extension added to the files.

     ![2023-12-21_18-05](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bdeb4db7-ed7f-41b8-8a2d-13ca197a08d4)

- After reading the /etc/passwd file,I decided to test the submit functionality of the web page, I uploaded a random file and it popped out an error that only pdf files are allowed.I tried  to upload a php shell and adding the ".pdf" extension to it.The error popped up again

  ![2023-12-21_18-15](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0084dcd8-2faf-415d-a912-4bc1d11cc24f)

- I tried the next technique on the list which is the magic bytes technique.It involves adding the magic bytes of the file in the allowedlist to our php shell.A pdf file's magic bytes is "%PDF-".

   ![2023-12-21_18-20](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8c3dd879-2db6-4d28-85a1-7e12f0307fea)

- The shell upload was successful afer the magic bytes change.

  ![2023-12-21_18-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c79c3749-185b-428e-a431-786b9bbfb455)

- I accessed the shell via path traversal and executed shell commands.Challenge solved
    ![2023-12-21_19-47](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/23cf69cf-dac5-4dc4-bb2f-23ac2ee261db)

