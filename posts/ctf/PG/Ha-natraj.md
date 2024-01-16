* * *
 ### LAB: HA-NATRAJ
 ### PLATFORM: Proving Grounds
* * *

### Enumeration

- Rustscan's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ee663e2f-90d7-472f-bfe8-b8dc3c437fd9)

- FFUF's result

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9e3766d6-ba8c-4890-8c68-278d2a16bee8)

- I discovered a file.php in console which vulnerable to LFI,I was able to read /etc/passwd

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/918847dc-63c5-49b7-bfc0-1b543ab51b7a)

- After reading a lot of stuffs on LFI,I read that I can elevate LFI to RCE by poisoning apache log files,I was able to read only the
`/var/log/auth.log` file and we can elevate to rce by trying to log in to ssh with a php shell as the username in order to force auth.log
file to log the shell.The `auth.log` file's main purpose is to log ssh authentication events.

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/13c8d38f-e58d-4702-b234-6e8e63c36fc2)

- Try to login to ssh with a php shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/050d1b62-f5fa-4a23-909c-4766b50fc8b6)
  
- Proof of remote code execution

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/89aa7e2f-f410-437e-be5b-3d67785402c7)

- We can get a revshell with this,now we have a stabilized shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dd5c6072-1f49-4e89-90b6-b64b44081ed0)

### PRIVESC

- The sudo version of this virtual version is vulnerable to `BARONSAMEDIT[CVE-2021-3156]`.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a730c648-12b2-4201-91f0-c66267536126)

- I got an exploit from this <a href="https://github.com/blasty/CVE-2021-3156">github repo</a>

- Root

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d3b91ed1-0418-4e50-9f70-8ef35e67b087)




  
