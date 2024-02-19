### LACTF 2024
  I participated in the LACTF competition 2024 with my friend Bl4ckanon and I solved 3 challenges[1 crypto and 2 web]

### Challenges

- Very-hot
- Flaglang
- Pogn


### Very-hot [crypto]

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/12f322c7-6b06-43da-99e4-16f8e16d11f2)

 This crypto is based on the asymmetric .The modulus was created with 3 primes [p,q,r] and the creator used a public key of `2**16 + 1= 65537` to encrypt the flag.

  ### Src.py
          from Crypto.Util.number import getPrime, isPrime, bytes_to_long
          from flag import FLAG
          
          FLAG = bytes_to_long(FLAG.encode())
          
          p = getPrime(384)
          while(not isPrime(p + 6) or not isPrime(p + 12)):
              p = getPrime(384)
          q = p + 6
          r = p + 12
          
          n = p * q * r
          e = 2**16 + 1
          ct = pow(FLAG, e, n)
          
          print(f'n: {n}')
          print(f'e: {e}')
          print(f'ct: {ct}')
 ### out.txt
     n: 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
     e: 65537
     ct: 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985
              
 ### Solution
 - I used factordb to get the prime-factors of the modulus

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a9c9f908-341c-406e-9ed4-da143a4e2bf7)

 - And I wrote a script to auto-solve it,instead of using (p-1)*(q-1) to get phi if we have 2 prime factors,I used (p-1)*(q-1)*(r-1) because we have 3 prime factors

            #! /usr/bin/env python3
            from Crypto.Util.number import *
            #modulus
            n = 10565111742779621369865244442986012561396692673454910362609046015925986143478477636135123823568238799221073736640238782018226118947815621060733362956285282617024125831451239252829020159808921127494956720795643829784184023834660903398677823590748068165468077222708643934113813031996923649853965683973247210221430589980477793099978524923475037870799
            # public key
            e =  65537
            #Cipher text
            c = 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985
            
            # prime factors
            p = 21942765653871439764422303472543530148312720769660663866142363370143863717044484440248869144329425486818687730842077
            q = 21942765653871439764422303472543530148312720769660663866142363370143863717044484440248869144329425486818687730842083
            r = 21942765653871439764422303472543530148312720769660663866142363370143863717044484440248869144329425486818687730842089
            
            #phi
            phi = (p-1)*(q-1)*(r-1)
            
            #Private key
            d = inverse(e,phi)
            
            #decrypting the flag
            
            flag = long_to_bytes(pow(c,d,n)).decode()
            print(flag)

### Flag

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9a7afe0a-1852-469a-b0ca-681f8a274efb)

### Challenge 3: Flaglang

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3a74107b-0ef1-4495-b951-9f99ca1ca555)


- The main objective of this challenge is to read the flag in a yaml file.The flag is saved as `Flagistan` in the yaml file.
 
 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e501607b-6130-46eb-ab1e-3a04cdf6d7d1)

- According to the source code,if you try to read the value of Flagistan via the `/switch`route. It will pop an `unauthenticated error[error 400]` because the route requires a password placed in the cookie to get the flag

        app.get('/switch', (req, res) => {
        if (!req.query.to) {
          res.status(400).send('please give something to switch to');
          return;
        }
        if (!countries.has(req.query.to)) {
          res.status(400).send('please give a valid country');
          return;
        }
        const country = countryData[req.query.to];
        if (country.password) {
          if (req.cookies.password === country.password) {
            res.cookie('iso', country.iso, { signed: true });
          }
          else {
            res.status(400).send(`error: not authenticated for ${req.query.to}`);
            return;
          }
        }
        else {
          res.cookie('iso', country.iso, { signed: true });
        }
        res.status(302).redirect('/');
      });

### Unauthenticated error

    ❯ curl https://flaglang.chall.lac.tf/switch?to=Flagistan
      error: not authenticated for Flagistan   

- To read the flag,I used the `/view` route because it doesn't request for any password to read the value of Flagistan

        app.get('/view', (req, res) => {
        if (!req.query.country) {
          res.status(400).json({ err: 'please give a country' });
          return;
        }
        if (!countries.has(req.query.country)) {
          res.status(400).json({ err: 'please give a valid country' });
          return;
        }
        const country = countryData[req.query.country];
        const userISO = req.signedCookies.iso;
        if (country.deny.includes(userISO)) {
          res.status(400).json({ err: `${req.query.country} has an embargo on your country` });
          return;
        }
        res.status(200).json({ msg: country.msg, iso: country.iso });
      });
      
### Flag
 
 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/52903ca5-eb73-4d21-8607-d26b3c52673a)


### Challenge 3: Pogm

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1e18a1f4-44f5-41ab-9cf3-eaa4d39635c1)

  This web challenge is based on a ping pong game and requests are made through websockets.According to a file `server.js`in the source code,the game reveals the flag if the ball pos
hits a score of 100

 
      // check if there has been a winner
      // server wins
      if (ball[0] < 0) {
        ws.send(JSON.stringify([
          Msg.GAME_END,
          'oh no you have lost, have you considered getting better'
        ]));
        clearInterval(interval);

      // game still happening
      } else if (ball[0] < 100) {
        ws.send(JSON.stringify([
          Msg.GAME_UPDATE,
          [ball, me]
        ]));

      // user wins
      } else {
        ws.send(JSON.stringify([
          Msg.GAME_END,
          'omg u won, i guess you considered getting better ' +
          'here is a flag: ' + flag,
          [ball, me]
        ]));

- I noticed some message codes used to interact with the server via websockets.GAME_UPDATE is sent if the game is still on and the ball pos is within the range of 0 and 100 ,GAME_END is also sent if the ball pos is lesser than 0 to end the game and if it is higher than 100 to send the flag.
      
       app.ws('/ws', (ws, req) => {
        const yMax = 30;
        const collisionDist = 5;
        const Msg = {
          GAME_UPDATE: 0,
          CLIENT_UPDATE: 1,
          GAME_END: 2
        };
  
      // check if there has been a winner
      // server wins
      if (ball[0] < 0) {
        ws.send(JSON.stringify([
          Msg.GAME_END,
          'oh no you have lost, have you considered getting better'
        ]));
        clearInterval(interval);

      // game still happening
      } else if (ball[0] < 100) {
        ws.send(JSON.stringify([
          Msg.GAME_UPDATE,
          [ball, me]
        ]));

      // user wins
      } else {
        ws.send(JSON.stringify([
          Msg.GAME_END,
          'omg u won, i guess you considered getting better ' +
          'here is a flag: ' + flag,
          [ball, me]
        ]));
        clearInterval(interval);

- I wrote a py script to send negative numbers to the server with websockets python library.I faced the hurdle of sending ball pos with the client_update message code [1],I kept losing to the server.

                value: str = json.dumps([1,[[i,i],[i,i]]])
                print("[+]Value:"+value)
                await websocket.send(value)

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0c2076ab-b0da-4523-b6f0-5da8b64e28a6)

- I decided to change the message code to GAME_END[2] and I started getting ball pos within the range of 0 - 50 till I got the flag.I really don't know the logic behind my answer but it takes time for the script to get the flag because of the numbers.You might need to try a couple of times to get the flag.Oops,what a mysterious solution  to a mysterious challenge.

 ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2b2f4b80-307c-4fba-9658-2b95fbe35153)
      
      #! /usr/bin/env python3                                         
      import websockets                                               
      import asyncio                                                  
      import json                                                     
      async def connect_to_websocket():                                     
            uri = "ws://pogn.chall.lac.tf/ws"                               
            async with websockets.connect(uri) as websocket:                    
                  for i in range(-10000,10000):                                         
                      resp = await websocket.recv()
                      print("First resp:"+resp)                                       
                      value: str = json.dumps([2,[[i,i],[i,i]]])                      
                      print("Value:"+value)                                           
                      await websocket.send(value)                                     
                      resp =await websocket.recv()                                    
                      print(f"2nd resp: {resp}")
                      if "lactf" in resp:                                                         n   
                          exit()
                                                                                                                                asyncio.get_event_loop().run_until_complete(connect_to_websocket())
