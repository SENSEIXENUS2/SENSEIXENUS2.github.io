![2023-12-23_23-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/31438e22-6795-4220-8a37-9a52d44693f3)* * *
### WEB-CACHE-POISONING
* * *

### CHALLENGE 1:
  Challenge description: Web cache poisoning with an unkeyed header
  
  ![2023-12-07_17-35](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/758db05a-0fc2-4c58-b6f1-e06aedaa85f9)

- Intercept the host page with burp suite

  ![2023-12-07_17-38](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6bffef9d-06cb-445f-821a-dbc91353ad96)

- Use param-miner burp extension to guess everything

  ![2023-12-07_17-40](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4621f7f7-4b22-4faf-94ad-8a71f5b2fc93)

- Param-miner spotted an hidden header
  
  ![2023-12-07_17-43](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/baead52a-0247-420d-92bc-f9fa7e8fde85)

- Send it to the repeater,you will notice that,inputing a couple of text will reflect on the webpage

  ![2023-12-07_17-48](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0aad8114-0dc3-4452-831c-9569048e015f)

- That header is vulnerable to reflected cross-site scripting,we can close the tag and execute javascript code

   ![2023-12-07_17-54](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0a10e38c-310c-4106-a6cd-0aec362cfd5e)

- And I got this response

   ![2023-12-07_17-55](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/11840455-f124-4f52-aadb-a4301272e32a)

- I solved the challenge with this payload

       "></script><script>alert(document.cookie);</script>
- Challenge solved

  ![2023-12-07_17-57](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6667bcbc-9fc1-498c-9d85-217c8622e4a9)

### Challenge 2:
   Challenege description:  Web cache poisoning with an unkeyed cookie

   ![2023-12-07_18-17](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/b17d8d9b-245a-4d20-b824-8483035c4909)

- Intercept the host page with burpsuite
  
    ![2023-12-07_18-19](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/bd983372-f47c-4ff6-a62c-31d76a64d2b9)

- Send to the repeater, the cookie param "fehost" is the vulnerable point, use this payload

      }</script><script>alert(1)</script>
- It reflects "1"

  ![2023-12-07_18-23](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/473745a8-f646-4cb6-87f0-c237ab335a19)

- Challenge solved

  ![2023-12-07_18-24](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/0dbbea9c-470e-4a73-9640-127ebb778e58)

  
### Challenge 3: 

  ### Web cache poisoning with multiple headers

  ![2023-12-23_22-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/592d26b1-9c35-46d0-8494-2d382116b8df)

- I intercepted the webpage request with burpsuite and checked the http history, I noticed that  this js file is being cached by the content delivery network.

  ![2023-12-23_22-52](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/29983f5f-7ed9-4dc2-ba56-230444dbbb1f)

- I fuzzed for headers with param miner burp extension, it spotted only X-Forward-Scheme and I also decided to test X-forwarded-host and it worked.X-forwarded-Scheme specifies " Specifies the scheme the client uses to make the request, such as “HTTP” or “HTTPS" " while X-forwarded-Host specifies the host requested by the client

 ![2023-12-23_23-01](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6a452118-b253-4a3d-af79-498c962a1540)

- Go to the exploit server,enter the payload "alert(document.cookie);", change the file value to "/resources/js/tracking.js" and store the exploit.The main goal is to force the Content Delivery Network to cache the malicious javascript file instead of the normal js file.

 ![2023-12-23_23-28](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e464bfda-6944-41fc-ac6a-af1e2d3ffdae)


- Change the value of x-forwarded-scheme to "http" and the value of x-forwarded-host to "exploit-0afa009b0457332185b93e1a016100f6.exploit-server.net" before sending to the server

   ![2023-12-23_23-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/14bf8564-54b9-4652-969f-277e1a72f173)

- The CDN has cached our malicious url

  ![2023-12-23_23-26](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/fc085553-2346-4fd7-8eed-6c39113b3bee)

- When a user opens the url "https://exploit-0afa009b0457332185b93e1a016100f6.exploit-server.net/resources/js/tracking.js",it redirects the user to our cached malicious page

    ![2023-12-23_23-57](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/2f4239c1-9f1e-406f-bf9c-f8134c09414d)

-   
    


