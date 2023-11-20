
# ReCaptcha v39
We are given a link to a website asking to solve Recaptcha v39

Upon visiting the link, the website tells us we need to solve the area of 100 images provided each within 5 seconds. Below is an exapmple of an image

![](https://github.com/0xNev/CTF-Writeups/blob/main/VSCTF23/ReCaptchav39/1.png?raw=true)

Upon checking network in devtools we see the captcha process happens over websocket. We'll make a Python script that automates the captcha.

Looking back I may have overcomplicated the script, but here's the process

 - Start a websocket session with the server
 - Download the image the server sends
 - Use OpenCV to make the shape solid
 - Calculate the pixels relative to the size given
 - Send the answer over the websocket session
 - Repeat 100 or so times
 - Get the flag

 
 I've added the script to the writeup directory
