* * *
  ### HTTP Host Header injection 
  ### Lab: Portswigger
* * *

### Challenge 1:
  Challenge description: Basic Password Attacks
  
   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/004526cb-e895-436f-ab4e-ab9bfed94548)

- Navigate to 'forgot password'

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/7d83c479-fe37-4a07-9c40-135d69b10dee)

- Reset Carlos' account and intercept with burpsuite

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/929f76b6-0822-4efa-8d11-afa66667914c)

- If we change the http host header value ,we will notice that it still forwards the request to the server and submits the data

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3d8d937f-b740-4901-92a4-4b84489daa5a)

- Replace the host header value with a burp collaborator link

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e45e788e-bf46-485e-8d9d-220fff65ad13)

- Wait for burp collaborator to log burp requests

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/484c2e97-2f61-4508-b162-ab342f94c79e)

- Add the token to "https://0abb00d5043a44e681fa4164009600f1.web-security-academy.net/forgot-password?temp-forgot-password-token=",
  load the url,change the Carlos' password and log in into Carlos' account.Challenged solved

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3f2deed0-04ef-4310-9234-a16760a1b29d)


   
