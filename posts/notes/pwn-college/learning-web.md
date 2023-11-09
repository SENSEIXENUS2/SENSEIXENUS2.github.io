* * *
### Pwn College's notes
* * *

- Making HTTP request with curl

      curl www.google.com
- Making HTTP request with nc

- Making HTTP request with python requests module

      import requests
      requests.get("http://127.0.0.1").content.decode()
- Setting host header with curl 

       curl <url> -H "Host: <anychar>"
- Using host header with python http request

      import requests
      headers = {"Host": "char"}
      request.get("url",headers= headers}
- Setting path in curl
    
      curl 127.0.0.1/bla/bla/bla
- setting path with python

      import requests
      requests.get("http://127.0.0.1/nla/bla/bla").content.decode()
- Using url encode in curl,url encode the character of the path with a urlencoder or use burpsuite url encoder,space is %20 in url encode

      curl 127.0.0.1/fd92086e%20857f36dd/19440651%20228056fc
- Using url encoded path with python

      requests.get("http://127.0.0.1/95d89500%201ddf62f6/00df8f70%2057620caf").content.decode()
-
    
