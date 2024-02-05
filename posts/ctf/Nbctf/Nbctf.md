### NBCTF's writeup

### Web Challenges

- Secret Tunnel
- Walter's crystal shop
### Secret Tunnel
  This challenge's source code contains 2 important files `main.py` and `flag.py`.The main vulnerability in this challenge is SSRF [Server Side Request Forgery].
This vulnerability allows an attacker to make a request to a particular location e.g if a service is made available internally which means a request cannot be made
outsie the network,an atacker can use server side request forgery to make a request to that service.

- `Flag.py` is running a flask application on port 1337 which is an internal service.The application reads the contents of flag.txt and serves
the content when a get request is made to  `http://127.0.0.1:1337/flag`.

        from flask import Flask, Response
        
        app = Flask(__name__)
        
        flag = open("flag.txt", "r").read()
        
        @app.route("/flag", methods=["GET"])
        def index():
            return Response(flag, mimetype="text/plain")
        
        if __name__ == "__main__":
            app.run(port=1337)

- `Main.py` allows users to make request with the aid of the `requests.get()` method.Sinc the flask application is running on the server,we can make a request to
http://127.0.0.1:1337/flag to get the flag.Although, the code restricts users from adding "127","x","flag" and using 2 dots to the url they want
to make a request to.
      
      #!/usr/local/bin/python
      
      from flask import Flask, render_template, request, Response
      import requests
      
      app = Flask(__name__,
                  static_url_path='',
                  static_folder="static")
      
      @app.route("/fetchdata", methods=["POST"])
      def fetchdata():
          url = request.form["url"]
      
          if "127" in url:
              return Response("No loopback for you!", mimetype="text/plain")
          if url.count('.') > 2:
              return Response("Only 2 dots allowed!", mimetype="text/plain")
          if "x" in url:
              return Response("I don't like twitter >:(" , mimetype="text/plain") 
          if "flag" in url:
              return Response("It's not gonna be that easy :)", mimetype="text/plain")
      
          try:
              res = requests.get(url)
          except Exception as e:
              return Response(str(e), mimetype="text/plain")
      
          return Response(res.text[:32], mimetype="text/plain")
      
      @app.route("/", methods=["GET"])
      def index():
          return render_template("index.html")
      
      if __name__ == "__main__":
          app.run()
### Bypassing the restrictions
- Instead of `127.0.0.1`, we can replace it with `localhost` because `localhost` is also a loopback address.This will also bypass the restrictions of the two dots.
To use the string "flag",we can url-encode one of the characters of the string "flag".
  
