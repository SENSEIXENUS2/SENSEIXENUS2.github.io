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
      
