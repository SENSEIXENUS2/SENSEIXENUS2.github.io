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

- Use "john --show <hashfile> to show password after cracking

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1109564d-67ad-4e72-8664-5de5ddfc4dd2)

- To crack use

      john <hashfile> --wordlist=<wordlist path>

 ### Extracting the archive

 - Extract the tar file with this command with this command

       tar -xvf <path to tar file>

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6671c59a-b66a-450a-8e03-8221a9c9bdeb)

- The README file states that the file is a borg backup repository,we can extract the archive with this binary "borg"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c245e340-dbb5-4fca-8532-225c999f6b1c)

- List the archive with this command
   
       borg list --json /path/to/repository

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ba24dcd7-129b-461d-bd77-36aaebeb7c7c)

- Extract the archive with this command

  
