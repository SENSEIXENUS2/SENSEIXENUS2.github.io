* * *
 ### Access Control Vulnerabilty
* *  *
### Broken Accesss Control
 Access control is the constraints on who is able to access a resources or perform a specific action.It depends on authentication and session management
### Types
- Vertical access control
- Horizontal access control
- Context dependent control

### Challenge 1:
 Challenge description: Unprotected admin functionality
 
 ![2023-11-08_02-04](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0d23173d-b9b9-4cbd-b15c-c506093e1548) 

- Access the robots.txt file of the page and the "Disallow" header disallows web crawler from finding administrator-panel
  
  ![2023-11-08_02-08](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/86233fe6-8a2c-47fd-b8d9-27b3174ce3f9)

- Making a request to the page will grant us access to the admin panel and with access to the panel I deleted the user 'carlos' and solved the challenge
  
  ![2023-11-08_02-11](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/15dc1610-b752-4fec-9275-7762b8523ae4)

 ### Challenge 2:
 Challenege description: Unprotected admin functionality with unpredictable URL

   ![2023-11-08_02-15](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/a4046b26-d94a-4759-a035-57cf8f41c1fd)

- In this challenge,the admin page is revealed in the source code and robots.txt is not available.

  ![2023-11-08_02-17](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/44a3f966-5a19-4748-9d09-f9102a684509)

- I accessed the page,deleted the user 'carlos'.Challenge solved

   ![2023-11-08_02-18](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/643274f6-116f-4cb5-9c93-34c6d5c8d34f)

### Challenge 3:
  Parameter based access control
  Some user access controls are determined with the aid of
- Hidden values
- Cookie
- Preset query string
  Challenge Description: User role controlled by request parameter
   ![2023-11-05_18-29](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/45b0695b-d4b0-4707-953f-2a30fa6140bf)

- Navigate to  /admin,you will notice an error message that you should login as an administrator

 ![2023-11-09_17-15](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/097ed22e-2669-435b-a79c-ccbb5a7940ab)

- Login into wiener's account,intercept the request with burp's proxy,forward it once and change the admin parameter to admin
  
  ![2023-11-09_17-11](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/458a5d27-12ec-401c-bd04-572d5b8046ba)

- We now have access to the admin page.To delete the user 'carlos',you should also intercept the request and swithc thr admin parameter to "true".
  ![2023-11-09_17-12](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2c561778-4e79-4b7a-bdcd-ac43aeb60b74)

- Challenge solved
  ![2023-11-09_17-13](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/89a4821e-50c9-4ded-93d5-f6d5fbd51c15)

### Insecure Direct Object Reference(IDOR)
 It is form of access control vulnerability that occurs when an application uses user-controlled input to control object.It is a form of vertical access control and can lead to vertical privilege escalation.
e.g
- Website parameter access to object
  
      https://insecure-website.com/customer_account?customer_number=132355

- Direct access to static files

      https://insecure-website.com/static/12144.txt
### Challenge 1:
  Challenge description:
  
![2023-11-05_18-17](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/83a09ffa-fd91-4bd0-85b5-bafde2c14bba)

- The main aim of the chalenge is to access carlos' text transcript

  ![2023-11-05_18-19](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1174c8de-bcb2-49e5-a419-af7fdb400b9e)
    
- I intercepted the download transcript request with burp and sent it to the repeater.In the response,I noticed a download path with a txt file.We can make a request to that url path and fuzz the number '3' digit to access other users chat.

  ![2023-11-05_18-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5e838bb4-b2c2-411d-86c8-fe191739016a)

- I made a GET request to this url.

       https://0aa9006a03e2f0ae8016da4d002c000f.web-security-academy.net/download-transcript/3.txt
- And I intercepted with burp suite proxy
    ![real](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/abe6e672-7db3-4174-a823-2c7cf705007c)

   
- I sent the request to the intruder functionality of burp suite and used the numbers payload type to fuzz.

  ![2023-11-05_18-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4af6df2e-abfe-4da7-880d-9e3deeb8a9fc)

- Number '1' revealed carlos' text transcript and  his password in it.

 ![2023-11-05_18-36](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/52eb72ed-c2e5-453b-8077-447cf9efd922)

- Challenge solved.

  ![2023-11-05_18-44](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1fa36540-572d-432a-8105-5ccad44e077c)

  

   
