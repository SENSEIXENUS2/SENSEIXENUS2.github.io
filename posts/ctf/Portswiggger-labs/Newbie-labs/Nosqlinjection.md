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

   
-
