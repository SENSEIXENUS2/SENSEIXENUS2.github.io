* * * 
  ### LAB: GAARA
  ### PLATFORM: PROVING GROUNDS[PG]
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/807171f4-fa18-47e3-911b-9fb01cb47d47)

### ENUMERATION
- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/17699a7d-e92c-4a07-8168-019ee8c80edb)

- I found nothing tangible after fuzzing for directories with ffuf

- I decided to bruteforce ssh with hydra.I used the username `gaara`.It worked,Hydra was able to find the password.
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/87f52e07-9bc0-4fb0-b98e-0c8f68902be1)

- SSH access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f6501a51-c020-4c8a-b6b0-b32ad3867918)


### PRIVESC
- I discovered that a gdb binary has SUID bit with this command `find / -perm -u=s -type f2</dev/null`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d9a6ac38-56c6-491e-b192-c7ac581378c4)

- I escalated privileges with this payload from gtfobins `gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/31c8ca52-c375-4ed2-a458-a2548976b730)
