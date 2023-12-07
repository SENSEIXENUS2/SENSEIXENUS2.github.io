* * *
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

  

