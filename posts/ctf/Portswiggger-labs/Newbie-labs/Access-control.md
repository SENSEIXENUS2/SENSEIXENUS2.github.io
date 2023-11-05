* * *
 ### Access Control Vulnerabilty
* *  *

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

- The main aim of the chalenge is to access carlos text transcript

  ![2023-11-05_18-19](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1174c8de-bcb2-49e5-a419-af7fdb400b9e)
    
- I intercepted the download transcript request with burp and sent it to the repeater.In the response,I noticed a download path with a txt file.We can make a request to that url path and fuzz the number '3' digit to access other users chat.

  ![2023-11-05_18-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/5e838bb4-b2c2-411d-86c8-fe191739016a)

- I made a GET request to this url.

       https://0aa9006a03e2f0ae8016da4d002c000f.web-security-academy.net/download-transcript/3.txt
- And I intercepted with burp suite proxy

  ![2023-11-05_18-29](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4ed03260-4397-4f49-9e61-2879a2daf01f)
 
- I sent the request to the intruder functionality of burp suite and used the numbers payload type to fuzz.

  ![2023-11-05_18-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4af6df2e-abfe-4da7-880d-9e3deeb8a9fc)

- Number '1' revealed carlos' text transcript and  his password in it.

 ![2023-11-05_18-36](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/52eb72ed-c2e5-453b-8077-447cf9efd922)

- Challenge solved.

  ![2023-11-05_18-44](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/1fa36540-572d-432a-8105-5ccad44e077c)

  

   
