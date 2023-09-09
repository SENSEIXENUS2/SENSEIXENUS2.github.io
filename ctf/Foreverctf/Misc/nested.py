#! /usr/bin/env python3
import subprocess
import re
def flagCheck(x):
    result = re.search(r"flag.txt",x.decode())
    if result != None:
        return True
    else:
        return False
while True:
      run = subprocess.Popen("unzip -o flag.zip",stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
      stdout,stderr = run.communicate()
      print(stdout)
      if flagCheck(stdout) == True:
          print(stdout)
          subprocess.run("cat flag.txt",shell=True)
          break
