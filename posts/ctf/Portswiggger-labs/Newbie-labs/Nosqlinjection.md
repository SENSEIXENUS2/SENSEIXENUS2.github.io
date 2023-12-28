* * *
 ### NOSQL Injection
 Lab: Portswigger
* * *

### NOsql injection
 
 An attacker is able to achieve if he is able to tamper with nosql database queries.A good example of a nosql database is mongodb.

### Types

- Syntax [Break a statement to insert your payload]
- Operator [Insert nosql operators]

Fuzz with this characters
'"`{
;$Foo}
$Foo \xYZ
Test it after url-encoding it “'%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00”

- If the response body is in json, you shouldn't urlencode it,it should be like this "'\"`{\r;$Foo}\n$Foo \\xYZ\u0000"
- To determine the error, use “this.category == ‘’' ”,don't forget to escape the quote “this.category == ‘\’' ”
- If the other payload doesn't trigger an error, the web application is vulnerable to an injection attack
- Test with boolean conditions to test for nosql ,test with a true statement “' && 0 && 'x” and a false statement “' && 1 && 'x”
- One of the statements will impact a server side query e.g you can trigger a js error ‘||1||’ or fizzy' || ‘1’=='1

### Challenge 1: 
   Challenge description: Detecting NoSQL injection

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/45956f80-b864-4302-92a5-d1eea81508e9)
   
- Navigate to one of the categories

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/ebba3b23-4393-4280-a865-52b5d7dc2253)

- Test the category query with one of true or false statements, the true statement worked lifestyle' || '1'=='1 and displayed all the unreleased products

  ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/01fcb6c5-5836-4e0d-9fb9-c1304bc7126f)

- Challenge solved

   ![image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/assets/98669513/80f9ecfe-facf-4905-b99d-8d0d6720372c)

### Challenge 2:
  Challenge description:
   
