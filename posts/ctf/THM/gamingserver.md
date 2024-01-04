* * *
  ### Lab: Gaming server
  TRYHACKME
* * *  

### Enumeration

- Rust scan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/26b330d0-1935-4add-bf3b-fd02405e16ff)

- Fuzzing for directories with ffuf

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dc77577a-9dc4-43d4-b34d-793aa40fdd2e)
  
- Checking the source page reveals a possible username 'john'
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ec60930b-df58-49c9-a0b7-907fa295c7bc)

- Robots.txt states a '/uploads/' directory

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/859cb049-ac9a-41f4-b123-76ae63188b52)

- 'Secret' contains a private ssh key

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b3de4bf6-1f59-4afe-bf7b-c1cbf936a430)

### Gaining access

- Get the hash for the ssh privtate key with ssh2john.py and crack with john

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/34575332-5c68-4941-aa99-031345eda8c8)

- Change the permissions on the sshkey with this command

      chmod 600 <ssh key>
- Ssh access
  
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bd6b009f-82eb-442a-8e56-1fa07982ffb9)

  
### Privilege escalation

- The Ubuntu version (UBUNTU 18.0.4.4 LTS) has a kernel exploit (overlayfs).I sent the exploit binary to the target machine with python http.server,compiled and changed the binary's permission.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5e145fa4-1707-4c1a-8292-160f6645455e)

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/013ef35f-45b7-4035-bd9a-41ad93307181)
