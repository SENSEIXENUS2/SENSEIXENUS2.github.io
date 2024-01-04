* * *
  ### Cyborg
  Lab: THM
* * *

### Enumeration

- Rustscan's result reveals ssh and http ports

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/01ec07d7-5e7c-43fe-81e0-88e6ae437d86)

- The port 80 shows a default apache page on a web browser

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/242114dd-beb5-4e06-b328-0903edb340d4)

- Scanning with ffuf reveals two directories "/etc" and "admin"

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2517b8bd-b2a1-42b6-ae20-c9eec55c162b)

- /etc contains a directory listing

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/50014ba8-700f-483d-a0db-85e77678bbd5)

- /admin reveals an admin page

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d0ebf82a-00e1-4ee0-8286-9c19cfe0124d)

### Important details  
- The admin's index.html page reveals the existence of a music archive file which I later discvered to be this "archive.tar" file

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e3726184-5caf-492d-b98d-7e06f1fca510)

- The /etc on the other hand contains an hash file which after cracking it will be the password for the archive

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4f0ac2c1-78ed-4f37-a8cb-3857f0b0787f)

### Cracking the hash with John



--
