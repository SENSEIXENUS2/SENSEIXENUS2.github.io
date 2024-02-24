### CTF: BRAEKERCTF


### Challenge:

- Empty execution [web]


### Challenge 1: Empty execution
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

### Creating a Payload

- The first step is to bypass the os.access() filter by ensuring that it returns True,
