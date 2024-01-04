* * *
 ### Lab: Tryhackme
 Overlayfs
* * *

### ROOM'S BACKGROUND
   This room is based on CVE-2021-3493 and it affects this linux(Ubuntu) versions.It is a kernel exploit for privilege escalation
- Ubuntu 20.10
- Ubuntu 20.04 LTS
- Ubuntu 18.04 LTS
- Ubuntu 16.04 LTS
- Ubuntu 14.04 ESM

- <a href="https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/THM/Compiled%20exploits/overlayfs">Link to exploit</a>

   The exploit is well explained in <a href="https://ssd-disclosure.com/ssd-advisory-overlayfs-pe">ssd disclosure</a>

### ROOM

- Access the server via ssh

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9f53e65e-f545-4825-abd0-a87d34f36bf9)

- Set up an http server with python on your machibe to get the file on the target machine

      python -m http.server 8000

- Receive the file on your target machine with wget

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b7576ab2-bf67-4acd-87c0-848566247733)

- Compile the exploit with this command on the host server and change permissions

      gcc -o littlebankai.c bankai

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a84ea6f1-00ff-4e23-b687-988a940093be)

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3ea1d401-5b9a-4013-83bd-ed7408d7aacb)
 
- Challenge solved  

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/06650b97-1328-476d-aac5-d43bee1dff19)

