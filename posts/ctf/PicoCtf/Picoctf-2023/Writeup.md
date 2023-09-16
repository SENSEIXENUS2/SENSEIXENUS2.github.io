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
  <p>The regex pattern matches any text with 7 characters but must start with small letter p and end with capital letter F to get the flag. </p>

# Flag

![Image](https://github.com/SENSEIXENUS2/SENSEIXENUS2.github.io/blob/main/posts/ctf/assets/Images/Pico2023/regex3.jpg)
