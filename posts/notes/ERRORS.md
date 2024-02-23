### Warning: failed to launch javaldx - java may not function correctly
   Typical Libre-office error

      sudo apt-get install default-jre libreoffice-java-common

### Virtualenv Runtime Error 
   Example of error
        
    RuntimeError: failed to query /usr/bin/python2.7 with code 1 err: '  File "/usr/local/lib/python3.10/dist-packages/virtualenv/discovery/py_info.py", line 152\n    os.path.join(base_dir, exe) for exe in (f"python{major}", f"python{major}.{minor}")\n                                                           ^\nSyntaxError: invalid syntax\n'


   You need to downgrade virtual venv

      pip install virtualenv==20.21.1
   Installing venv
     
      pip install virtualenv

   Creating venv

      virtualenv -p <path to python bin> <virtual env name>
   Activating it

     source <venv name>/bin/activate

  Deactivating it

      deactivate
### Some index files failed to download. They have been ignored, or old ones used instead.(apt-key) errors

      sudo apt-get install --reinstall coreutils

### Fixing infinite login issue
   The error occurs if .Xauthority ownership is assigned to root account and not to the user account

     use ctrl+alt+f1 to enter terminal mode
     enter login details
     locate .Xauthority
     chown username:username /home/<username>/.Xauthority
     reboot
      
### some app icons broken due to gdk-pixbuf and svg 

      sudo dpkg --configure -a

### Linux booting to initramfs mode 

    fsck /dev/sda1
         
### ImportError: cannot import name 'ParameterSource' from 'click.core'

     sudo apt purge python3-click
     sudo pip install click==8.1.6

### /bin/bash^M: bad interpreter:
     sed -i -e 's/\r$//' <script name>

### Enter passphrase for key 'id_rsa':sign_and_send_pubkey: no mutual signature supported

        ssh -o PubkeyAcceptedKeyTypes=ssh-rsa -i id_rsa <user>@<ip>

### Error in ysoserialize.jar while exploiting  CVE-2015-7501 

 `Error while generating or serializing payload
com.nqzero.permit.Permit$InitializationFailed: initialization failed, perhaps you're running with a security manager
        at com.nqzero.permit.Permit.setAccessible(Permit.java:22)
        at ysoserial.payloads.util.Reflections.setAccessible(Reflections.java:17)
        at ysoserial.payloads.CommonsCollections5.getObject(CommonsCollections5.java:83)
        at ysoserial.payloads.CommonsCollections5.getObject(CommonsCollections5.java:51)
        at ysoserial.GeneratePayload.main(GeneratePayload.java:34)
Caused by: com.nqzero.permit.Permit$FieldNotFound: field "override" not found
        at com.nqzero.permit.Permit.<init>(Permit.java:222)
        at com.nqzero.permit.Permit.build(Permit.java:117)
        at com.nqzero.permit.Permit.<clinit>(Permit.java:16)
        ... 4 more`

   ### FIX     

 - Install jdk 8 [link to jdk 8](https://builds.openlogic.com/downloadJDK/openlogic-openjdk/8u402-b06/openlogic-openjdk-8u402-b06-linux-x64-deb.deb)
 - The use `sudo update-alternatives --config java` to pick jdk 8

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3193cce5-59d4-4829-8d31-a39f4b563596)


