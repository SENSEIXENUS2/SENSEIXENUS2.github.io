<head><h1>Picoctf2023-writeup</h1></head>
<p>I played PicoCTF 2023 but I was too busy to document the way I solved the challenges.I played the ctf alone,these are the web challenges that I solved</p>

- MatchtheRegex
- More Sqli
- 


# MatchtheRegex
![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/regex-1.jpg)

<p>Task: Match a regex pattern to get the flag</p>

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/regex1.jpg)

<p>I viewed the source code and discovered this commented regex pattern in the code</p>
  
     // ^p.....F!?

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/regex2.jpg)

# Regex meaning
  <p>The regex pattern matches any text with 7 characters but the text must start with small letter p and end with capital letter F to get the flag. </p>

# Flag

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/regex3.jpg)

# More Sqli

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/sqli0.jpg)

<p>Task:Find the flag on the website</p>

# Approach

- I presumed that it will be sql injection since the name of the challenge is sqli and the hint says "SQLITE".
<p>The website has a login page</p>

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/sqli2.jpg)

<p>I tested the page text field with quote(') to trigger an sql error.I got this error</p>

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/sqli3.jpg)

<p>To bypass the page,the payload should be sent with the password text field.I used the payload [' or 1=1--+] but I url-encoded it to use it via cURL.</p>

# Flag
![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/sqli1.jpg)
