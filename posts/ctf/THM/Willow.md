* * *
 ### LAB: WILLOW
 ### PLATFORM: TRYHACKME
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7e7b3ca9-25f8-47cb-a65d-79388fab32ef)

### ENUMERATION
- Rustscan's scan details

        .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      🌍HACK THE PLANET🌍
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 10.10.196.134:22
      Open 10.10.196.134:80
      Open 10.10.196.134:111
      Open 10.10.196.134:2049
        
        PORT     STATE SERVICE REASON  VERSION
        22/tcp   open  ssh     syn-ack OpenSSH 6.7p1 Debian 5 (protocol 2.0)
        | ssh-hostkey: 
        |   1024 43:b0:87:cd:e5:54:09:b1:c1:1e:78:65:d9:78:5e:1e (DSA)
        | ssh-dss AAAAB3NzaC1kc3MAAACBAJHkiuOeIrYxoyBBsJX2wpThJlvbsanlxpYXyHspzVIdeGQq3kD/2h1iNbOLwIb/iwS4oaY83OwxMiXImgKm/QgpgffrrKmU41eI/q9i+3NhLfHLvoT5PWupe/UW5Y3/lfmIMD1UXTUJNYiA07w/kHKj9ElQs7EZ2oZ9L5j2/h/lAAAAFQDE3pT3CTjQSOUOqdgu9HBaB6d6FwAAAIAFWqdfVx3v+GNxecTNp1mDb64WZcf2ssl/j+B6hj5W7s++DTY7Ls/i2R0z5bQes+5rMWYvanYFyWYEj31qWmrLvluJbJKldG3IttW5WfMzIyOJ11MHGAMP2/ZXZ4w3t8dMMudgBPkXE1uGv+p03A1i+Z6UfvGVv4HrtlCwqCRBywAAAIBpf+5ztR5aSDuZPxe/BURQIBKqDhOVZOt+Zhcc1GEcdukmlfmyH0sSm/3ae4CYLqBgD1zzwwSg4IkPR8wb1wa3G5F+OSYymEoKuxYWYN4LlSe9vrIap/1C/NO+jMQ5ru6WYqBcNdPqHQ4r5I7MzhziLdNIhfBmY076aL2Dr/OsAg==
        |   2048 c2:65:91:c8:38:c9:cc:c7:f9:09:20:61:e5:54:bd:cf (RSA)
        | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC0/BxHjpZXU3EhwOMURG/xIJno/fZBBw2tntPhQMsA+L6YoVL4IyTKTz6SGM6BcX9622CGutBiO0pc0vhGlf9v/4cUB7My3d1r3t3EkNF0SaKAmAZLm8QOFbmS/TyHy9wF5TGJLunz5cN3NdGIz3Bz2GHHouicRo/vopYmHxjItfVgVUD2u+e5Gkw7u+U1BxZOrQDlaUS41AJvZm9Pk0pn2hWXeGTCJu8oyCqaEi/u8Wu7Ylp/t15NjEpiDpRp2LH9ctB3EG50LL+ti2o8/U652wIoNhnoF33eI6HJget9jvSC03oOx5r6NqHbOn94kVAUjFbYzK716dBa+I5jocHr
        |   256 bf:3e:4b:3d:78:b6:79:41:f4:7d:90:63:5e:fb:2a:40 (ECDSA)
        | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIW2cLhyEIs7aEuL5e/SGCx5HsLX1a1GfgE/YBPGXiaFt/AkVFA3leapIvX+CD5wc7wCKGDToBgx6bkIY9vb0T0=
        |   256 2c:c8:87:4a:d8:f6:4c:c3:03:8d:4c:09:22:83:66:64 (ED25519)
        |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOsXsk2l13dc4bQlT0wYP6/4gpeoTx5IfVvOBF++ClPu
        80/tcp   open  http    syn-ack Apache httpd 2.4.10 ((Debian))
        |_http-title: Recovery Page
        | http-methods: 
        |_  Supported Methods: GET HEAD POST OPTIONS
        |_http-server-header: Apache/2.4.10 (Debian)
        111/tcp  open  rpcbind syn-ack 2-4 (RPC #100000)
        | rpcinfo: 
        |   program version    port/proto  service
        |   100000  2,3,4        111/tcp   rpcbind
        |   100000  2,3,4        111/udp   rpcbind
        |   100000  3,4          111/tcp6  rpcbind
        |   100000  3,4          111/udp6  rpcbind
        |   100003  2,3,4       2049/tcp   nfs
        |   100003  2,3,4       2049/tcp6  nfs
        |   100003  2,3,4       2049/udp   nfs
        |   100003  2,3,4       2049/udp6  nfs
        |   100005  1,2,3      42540/tcp6  mountd
        |   100005  1,2,3      43340/tcp   mountd
        |   100005  1,2,3      48359/udp   mountd
        |   100005  1,2,3      53614/udp6  mountd
        |   100021  1,3,4      40759/tcp6  nlockmgr
        |   100021  1,3,4      45186/udp   nlockmgr
        |   100021  1,3,4      50445/udp6  nlockmgr
        |   100021  1,3,4      58835/tcp   nlockmgr
        |   100024  1          35734/udp   status
        |   100024  1          39889/tcp6  status
        |   100024  1          46758/tcp   status
        |   100024  1          60168/udp6  status
        |   100227  2,3         2049/tcp   nfs_acl
        |   100227  2,3         2049/tcp6  nfs_acl
        |   100227  2,3         2049/udp   nfs_acl
        |_  100227  2,3         2049/udp6  nfs_acl
        2049/tcp open  nfs     syn-ack 2-4 (RPC #100003)
        Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
                


- The page contains an encrypted string which I suspected to be in hex

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3f84ca00-69c1-4159-920f-d34212b6ef68)

- I used python decode it with bytes.fromhex() function and I got this message and some numbers

        ❯ python3
      Python 3.11.6 (main, Oct  8 2023, 05:06:43) [GCC 13.2.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>> import requests;from bs4 import BeautifulSoup
      >>> r = requests.get("http://10.10.196.134/").text
      >>> bs = BeautifulSoup(r,"lxml")
      >>> bytes.fromhex(str(bs.find('p')).split('<p>')[1].split('</p>')[0])
      b"Hey Willow, here's your SSH Private key -- you know where the decryption key is!\n2367 2367 2367 2367 2367 9709 8600 28638 18410 1735 33029 16186 28374 37248 33029 26842 16186 18410 23219 37248 11339 8600 33029 35670 8600 31131 2367 2367 2367 2367 2367 14422 26842 9450 14605 19276 2367 11339 33006 36500 4198 33781 33029 11405 5267 8600 1735 17632 16186 31131 26842 11339 8600 35734 14422 35734 8600 35670 2367 18410 35243 37438 14605 33781 33029 37248 8600 28374 2367 22149 27582 3078 2367 17632 9709 17632 5267 27582 8600 27582 23721 11405 13256 33985 37248 18278 33985 27582 26775 23721 26775 27582 22149 3078 3078 9709 11405 33985 18278 17632 37248 37248 33443 8600 18278 18278 27582 18330 13256 14422 14422 28061 10386 23219 10386 3339 25111 22053 21889 31131 33856 3339 16186 28061 7496 14605 22149 5851 35243 11339 33985 35243 22872 33443 33856 33443 22149 33856 8452 11339 7568 22053 22149 3947 29609 9709 35243 5851 11405 18199 13256 33215 33985 7568 33215 12244 5444 22053 14605 10386 7496 33215 3339 9709 10386 21889 8452 28061 28374 8499 12792 18199 20172 19276 8499 14422 22102 19396 12244 28061 23721 8452 27582 5851 19276 28374 12244 23721 26775 28374 18199 35243 13256 28927 23219 35243 35734 3339 33215 3339 22149 36500 14605 21404 27582 1735 35243 28638 12792 7496 27582 28061 33856 33856 28927 7568 11339 37438 37438 8452 3078 28374 28638 3339 9709 28927 28638 35243 19276 35734 4198 7914 18278 8600 37248 9709 18199 19276 20172 22149 14422 5444 11339 7496 12792 28638 7568 18199 29655 35243 21889 18199 12792 20172 31131 21404 20172 37248 33443 22053 21889 11339 7358 11339 21889 25111 5851 17632 21404 8499 12244 27582 21889 7496 37438 37248 21889 35734 33215 12244 8499 23219 18199 12792 31131 35670 12244 28638 37248 28927 28374 1735 4198 19396 8600 8600 27582 17632 20172 23219 29609 27582 8499 26775 27582 14422 13256 18199 9709 29609 1735 8600 20172 28638 7568 28927 35734 8600 18410 3339 7496 19276 3078 22149 29655 18278 18278 17632 31131 7568 31131 7358 11405 9450 8452 22053 9450 13256 33856 7914 8452 36500 17632 7358 3947 33215 28638 11339 18278 35734 28374 23721 11339 5444 29609 27582 17632 33215 22872 21889 18199 3078 11339 17632 5444 33006 8452 28374 33215 8499 14422 28374 33856 12244 35670 22149 10386 36500 22102 12244 7568 5444 11405 26775 13256 11339 31131 20172 2950 7358 16186 21889 33215 3339 8499 7568 23219 22053 35670 33006 29655 22872 23721 23787 35243 26842 7568 26775 19396 12244 19396 3947 27582 10386 7496 27582 35734 33215 5444 33856 29655 20172 12244 14605 25111 2950 23787 8499 28061 3947 21404 18199 31131 7358 18330 14422 28061 3078 21889 22872 28927 33985

- I enumerated for shares with `showount -e <ip>` and I mounted the shares with mount

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a7de6d78-07c0-46b1-8bbd-8653853e2e46)

- In the `/var/failsafe` directory,I discovered a text with rsa public and private key pair

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/06335668-21ce-4f6e-8cd1-b3f2eb1db544)

- Since we have the private key and modulus,we can easily decode the numbers with python,I wrote a script to automate the whole process

        #! /usr/bin/env python3
        import requests
        from bs4 import BeautifulSoup
        from Crypto.Util.number import *
        # retrieving the data from the site *add your machine_ip to the script[format http://<ip>]
        r = requests.get("<your target address>").text
        bs = BeautifulSoup(r,'lxml')
        rsa_numbers = bytes.fromhex(str(bs.find('p')).split('<p>')[1].split('</p>')[0]).decode().split('\n')[1]
        #Creating rsa_numbers and writing to it
        rsafile = open("rsa_numbers.txt","w")
        rsafile.write(rsa_numbers)
        rsafile.close()
        ## Ciphertext
        ct: list = open("rsa_numbers.txt","r").read().split(" ")
        #Removing the last empty string
        ct.pop()
        #Creating a file `willow_rsa` to store the key
        file = open('willow_rsa',"w")
        #private key
        d = 61527
        #modulus
        n = 37627
        
        #Decrypting the key
        dec_key = ''.join(long_to_bytes(pow(int(c),d,n)).decode() for c in ct)
        print(dec_key)
        print("[+]Writing to a file named willow_rsa")
        file.write(dec_key)
        file.close()

- The script's result reveals a private ssh_key

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ec741585-805c-4e7c-ba4b-097127e301b0)

- The private key requires a passphrase to login,I was able to retrieve the hash with sshjohn and cracked it with John the ripper

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bfcdbc76-857f-4d0e-8175-aa3fca53705d)

- SSH access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/95adccb6-2016-4e05-b1d4-c364bdbe3778)

### PRIVESC

- `Sudo -l` reveals that we can mount partitions in /dev directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/07a18693-9ef4-4248-aa08-aedb1cdc60f7)

- In /dev,I spotted an unmounted partition known as hidden backup which I mounted to /mnt directory,I later spotted a text file which contains
the root user password

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/90dbdcb7-ec0a-4e03-8238-1ea1a2a4c9ac)

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b0582e91-903d-4730-b891-d68e34f4f05c)

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1f4ce56b-9edd-4d4d-9648-41bae2735330)

### Flags

- The root.txt and user.txt are stored in /home/willow/user.jpg with steganography(hidden in plainsight).

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1ee1ed16-4394-45da-86b2-dd45b123bfd9)

- Access the file by copying it to the nfs share `/var/failsafe`

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9d2d9b5b-825a-4111-8607-7c831dcc5dc3)

- To get user.txt,use pytesseract python module

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0e0c2ca7-0625-4d39-a7de-e704ec07f01b)

- To get root.txt,use steghide to extract the text file from user.jpg,the password is the root user's password

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3f386ebf-ba37-4a88-ac13-d9d96655c3e2)

  
  
