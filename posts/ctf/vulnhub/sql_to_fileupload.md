* * *

### FROM SQL TO SHELL
Lab: Vulnhub
Vulnerabilities: SQLI,FILE UPLOAD BYPASS  
* * *

- Scan for hosts with netdiscover

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5f53dfd8-d7b4-4b2e-a897-19ce88bc5b25)

- Fuzz for directories and pages with gobuster

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/efc41c6a-71f7-4e29-bbc4-24660b7ba1ae)

- Testing this url "http://192.168.184.132/cat.php?id=1%27" with "'" will trigger an sql error which signifies that the parameter is vulnerable to sql injection

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0762f933-257a-49b1-bce1-428910144fef)

- Automate the exploitation with sqli,dump the admin's hashes and crack with sqlmap

       sqlmap -u "http://192.168.184.132/cat.php?id=1" -D photoblog -T users -C login,password --dump
    
   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ea26a5f7-56d7-4211-87d3-2e08df167e98)

- Login into the admin panel,it has a file upload page,let's see if we can upload a shell

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/11cc0cc8-2440-4baf-bf66-8bf242bb96dc)

- It doesn't allow php file,we can try to bypass it by changing the file extension to ".pHP"

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9af61a2e-bc80-4b9a-8277-a8d581a28492)

- We have successfully bypassed the shell with the pHP extension

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1b1a1a37-5466-4da4-b1b2-5b613528032f)

- Fuzz the admin directory for other sub-directories with gobuster

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/69160fd9-f43d-4da4-950c-e3e443c20b23)

- Gobuster spotted a directory that stores image uploads,now we can access our shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6d02458f-457c-411b-b4f3-711b5a4451d4)

- Challenge solved
