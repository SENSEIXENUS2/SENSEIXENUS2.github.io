* * *
### LAB: THM
###   BOUNTYHACKER
* * *

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f544ca59-80ed-428c-9c5a-1f60fb0814e5)

### ENUMERATION

- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/902e24af-4946-46f0-87fc-74238abb5e47)

- FTP has anonymous login and contains 2 files

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e9475535-c545-4a61-b4bd-bb91921b42bd)

- Locks.txt contains a wordlist to bruteforce Lin's account

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a15e57c0-7166-44da-b8a4-c440ec487350)

- task.txt reveals a possible ssh account "lin"
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/65271f37-3fb6-42cc-8cdc-2a0d654bdb0a)
 
- SSH access gained via bruteforce with Hydra

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dc40c5cf-c39b-400f-b914-5158d01928db)

### PRIVESC

- Sudo -l reveals that we can run tar as root without password which we can use to escalate privileges

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/22ce3989-922a-4a4b-9a55-dc0b21e511eb)

- I got the privesc method from gtfobins

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c951f458-516e-4bff-bcdc-39948ea2ffd3)

- Root access

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/28c35419-469f-49ee-a5d8-003ca82ac6bb)

  
   
