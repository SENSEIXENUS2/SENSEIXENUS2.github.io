* * *
 ### LAB: SMAG GROTTO
 ### PLATFORM: THM
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7a453ce7-6d04-4b62-b13e-ca2f9d6a8107)

### ENUMERATION

- Rustscan's details

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3959e905-9cf5-4b2c-885d-6539d0b24e76)

- Fuzzing directories with FFUF reveals '/mail/'
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8e15c7fe-78af-4781-94f4-95987e8de4f7)
  
- I saw a pcap file in the page of mail'directory which I analysed with wireshark and got a username and password for a subdomain
`development.smag.thm` which is a virtual host

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9bd13b5d-0318-4e3a-ad88-eb2028f4c3b0)

- I added it to my /etc/hosts file in this format `<machine_ip> development.smag.thm` to make it accessible on my computer 

- Accessing the domain with the login credentials reveals a page for command execution,we can pop a revshell with it

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f984a265-dfa5-42de-81e0-741f9d5dad87)

- Shell access

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1b4913aa-a54a-44e7-8e87-3743daa00932)

### PRIVESC

- The server runs a cron job that copies Jake's public key to his ssh authorized_keys,since the file is writable,we can copy our
ssh public key to his authorized keys and access his account without a password,you can generate a sshkey with `ssh-keygen -b 4096`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d8d631f6-3721-439a-8803-75bb5f052513)

- Jake's account accessed

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/39bb17a6-1279-418e-948f-ca3808d147eb)

- `sudo -l` output states that we can run `sudo apt-get` without password and with root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8d51d8d0-7877-4cea-a764-504cd5acc2a7)

- I was able escalate privileges with this one-liner from gtfobins

      sudo apt-get update -o APT::Update::Pre-Invoke::=/bin/sh

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fb28e34e-41b3-4b9e-82d6-9fac662a6fdc)

   
### UNINTENDED METHOD TO ESCALATE PRIVILEGES

- Overlayfs exploit can be used to escalate privileges on the server

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/96683b33-3f8c-4436-8e37-685cc6a297c5)


  
