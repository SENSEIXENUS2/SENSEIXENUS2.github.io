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
