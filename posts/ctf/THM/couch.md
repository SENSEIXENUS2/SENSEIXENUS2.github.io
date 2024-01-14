* * *
 ### LAB: COUCH
 ### PLATFORM: TRYHACKME
* * *
![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a104cfd1-ffd9-43e7-a1f3-a9f453a2d6a7)

### ENUMERATION
- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1c770c96-6287-4450-b44b-58cd3b038f2d)

- Nmap's service detection

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dc0b30d8-7982-473c-9930-3c4547640b60)

- I identified the web path with a walkthrough by tutorialspoint on COUCHDB [<a href="https://www.tutorialspoint.com/couchdb/couchdb_quick_guide.htm">Documentation</a>]
- Path "/_utils" provides the database administration tool

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1f103828-1db1-4e37-847f-319eb0330a3f)

- Path "_all_dbs" shows all the dbs hosted on that service

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9bb59621-bcd1-4e3b-99cd-489a2e5d8209)

- The secret db reveals a ssh login and password

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/34cd4b97-df92-465e-a6d6-017f16c7b2ed)

- SSH access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c66b337a-a07c-42e3-8dd0-2b1e574d7737)

### PRIVESC WITH DOCKER BREAKOUT

- Command `netstat -antp` reveals a possible internal docker service running on port 2375

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3ea6a7d9-3256-4329-8dd2-1bbcfa26493a)

- We can check if there is a docker image on the service with `docker -H <ip>:<port> info`.There is a docker image but with no container.

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d3be6360-1f1a-4584-8ab2-b29084f848bd)

- We can escalate privileges with this payload

      docker -H <IP>:2375 run --rm -it --privileged --net=host -v /:/mnt alpine
      chroot /mnt
- Root access

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/88e5a2ee-5649-4d52-bbf7-65898c2dab1d)
