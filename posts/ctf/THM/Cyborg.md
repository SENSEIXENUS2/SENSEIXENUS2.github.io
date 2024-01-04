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

- Extract the archive with this command,--list is for verbosity

       borg extract --list <repo path>::<archive_name>
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/34555d0b-b9dc-427b-85d2-cdd61cfe32f5)

- I spotted 2 files that might contain sensitive info

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9e7f9888-520d-4636-ad69-a37acebab7e1)

- "Note.txt" contains credentials for ssh

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/504f4020-ccbb-4824-b85c-c1ae77900c8f)

- Ssh access

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d14c0e8f-f8dd-463d-b294-d64e83dcf666)

### Privilege escalation

- "sudo -l" reveals a bash script that has access to sudo without need for a password

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1400aeba-e953-42d9-a653-2b2b866aaff1)

- Reading the source code reveals that it takes in "-c" flag and execute the input as a shell command

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4f132045-ffde-4c00-9578-a513a51e01b2)

- We can use it to escalate privileges or read "root.txt"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6b18ef20-0d0d-4310-aa16-2ce95f0dec5f)

  
- Challenge solved

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/175e188e-d56d-40ac-ad48-c0f4f84941b2)
