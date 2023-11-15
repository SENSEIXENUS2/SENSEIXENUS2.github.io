* * *
### Pwn College's notes
* * *

- Making HTTP request with curl

      curl www.google.com
- Making HTTP request with nc

      nc localhost 80
      GET / HTTP/1.1

      HTTP/1.1 200 OK
      Server: Werkzeug/3.0.1 Python/3.8.10
      Date: Mon, 13 Nov 2023 08:19:08 GMT
      Content-Length: 58
      Server: pwn.college
      Connection: close

- Making HTTP request with python requests module

      import requests
      requests.get("http://127.0.0.1").content.decode()
- Setting host header with curl 

       curl <url> -H "Host: <anychar>"
- Setiing host header with nc

      nc localhost 80
      GET / HTTP/1.1
      Host: b1f260b6f57036da290401094fe52a9a

      HTTP/1.1 200 OK
      Server: Werkzeug/3.0.1 Python/3.8.10
      Date: Mon, 13 Nov 2023 08:29:02 GMT
      Content-Length: 58
      Server: pwn.college
      Connection: close

- Using host header with python http request

      import requests
      headers = {"Host": "char"}
      request.get("url",headers= headers}
- Setting path in curl
    
      curl 127.0.0.1/bla/bla/bla
- Setting path with nc

      nc localhost 80
      GET /6927a3937537854a2639938f0bbee747 HTTP/1.1
- setting path with python

      import requests
      requests.get("http://127.0.0.1/nla/bla/bla").content.decode()
- Using url encode in curl,url encode the character of the path with a urlencoder or use burpsuite url encoder,space is %20 in url encode

      curl 127.0.0.1/fd92086e%20857f36dd/19440651%20228056fc
- Using url encoded path with python

      requests.get("http://127.0.0.1/95d89500%201ddf62f6/00df8f70%2057620caf").content.decode()
- Using urlencode path with nc

      GET /0f463741%202ef8eb45/5f0ef982%20d1f779eb HTTP/1.1

      HTTP/1.1 200 OK
      Server: Werkzeug/3.0.1 Python/3.8.10
      Date: Mon, 13 Nov 2023 08:51:33 GMT
      Content-Length: 58
      Server: pwn.college
      Connection: close
      
- Specifying an argument with curl

       curl 127.0.0.1?a=127fd9f9203241480df743a842646d93
- Specifying an argument with nc

      nc localhost 80
      GET /?a=dcbcdd2e90096d09ffbe419bb7834bd7 HTTP/1.1

      HTTP/1.1 200 OK
      Server: Werkzeug/3.0.1 Python/3.8.10
      Date: Mon, 13 Nov 2023 09:06:12 GMT
      Content-Length: 58
      Server: pwn.college
      Connection: close
  
- specifying an argument with requests python module

       import requests
       requests.get("http://127.0.0.1?a=9c7bd0be9e5100682c698e06309c5d7c").content.decode()
- Specifying multiple arguments with nc

      nc localhost 80
      GET /?a=c2bb4fdc1b23c61fc98efbb32e26111f&b=2656afe5%2016e8a17b%26e767498c%23031beb86 HTTP/1.1

      HTTP/1.1 200 OK
      Server: Werkzeug/3.0.1 Python/3.8.10
      Date: Mon, 13 Nov 2023 09:01:56 GMT
      Content-Length: 58
      Server: pwn.college
      Connection: close

- Specifying multiple arguments with curl

      curl -G 127.0.0.1 --data-urlencode "a=fc295d34898d1428b3ee1a4e77c006ef" --data-urlencode "b=d8ba5854 328b10e3&5046ff16#4c3b542a"
- Specifying multiple arguments with python

      import requests
      #specify the params
      params = {"a":"fb4cd6561b835e77a549381b106e66e2","b":"0ba5fb7b 38eb3acc&d94dea25#579e1d5d"}
      requests.get("http://127.0.0.1",params=params).content.decode()
- Including form data with curl

      curl 127.0.0.1 -d 'a=zzzzz'
- Including form data with nc

      nc localhost 80
      POST / HTTP/1.1
      Content-Type: application/x-www-form-urlencoded
      Content-Length: 34

      a=cd9a0a241c1ef407f5c21363db4dfdb3                                
- Including formdata with python

      import requests
      data = {"a":"0db2d6ac267531b853cea7825d4c3452"}
      requests.get("http://127.0.0.1",data=data).content.decode()
- Including multiple arguments with curl

      curl localhost:80 -d 'a=3177d16c7bdd39a040ed22e8e78fa94e&b=38cb5036 2589e771%269e2a9c5f%23c5152958'
- Including multiple formdata with nc

       nc localhost 80
- Including multiple formdata with python

       import requests
       data = {"a":"55cbd1e34f0886e3e081d8289a832598","b":"f5cd1473 408dace5&0b5015a1#ae9e7e53"}
       requests.post("http://127.0.0.1",data=data).content.decode()
- Making request with json data via curl
  
       curl 127.0.0.1:80 -H "Content-Type: application/json" -d '{"a":"1f977eb2be93af9168dd94806842ecc2"}'
- Making json data requests with python

      import requests
      import json
      data = {'a':'anychar'}
      headers = {"Content-Type": "application/json"}
      requests.get("http://127.0.0.1/",headers = headers,data = json.dumps(data))
- Sending complex json data with curl

    

