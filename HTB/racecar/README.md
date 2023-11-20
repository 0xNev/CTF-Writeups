
# Racecar
We are given a nc command and the bianry.
```bash
nc <someip> <someport>
```
![](https://github.com/0xNev/CTF-Writeups/blob/main/HTB/racecar/1.png?raw=true)

Some sort of racing game. Lets run some checks.

![](https://github.com/0xNev/CTF-Writeups/blob/main/HTB/racecar/2.png?raw=true)

A secure binary.

Let's decomplie it in Ghidra.

![](https://github.com/0xNev/CTF-Writeups/blob/main/HTB/racecar/3.png?raw=true)

Here's main, nothing too interesting.
Taking a look around, I found a function which loads in the flag, then asks for a user input and finally runs printf on the input.

![](https://github.com/0xNev/CTF-Writeups/blob/main/HTB/racecar/4.png?raw=true)


Running printf on a input we control is dangerous, this is our target vulnerability!

We first need to win a race in the program, which was very simple. Just choose the fastest car and most times you will win. Once we win we can try our theory. I started by trying to input %s but was unsuccessful. I instead had to use %x which was successful. Since the flag is up further on the stack we would need a couple %x's to leak the flag.

![](https://github.com/0xNev/CTF-Writeups/blob/main/HTB/racecar/5.png?raw=true)

Now that we've leaked a good amount of the stack we'll now need to figure out where the flag starts. I started plugging in each hex variable into cyberchef to see I could get a recognizable flag. Eventually I found '7b425448' was the start of the flag. I then automated the rest of the values in python

```python
from pwn import *  
  
hexed = "7b425448 5f796877 5f643164 34735f31 745f3376 665f3368 5f67346c 745f6e30 355f3368 6b633474 7d213f"
  
flag = ""

for x in hexed.split():
	flag = flag + unhex(x).decode()[::-1]

print(flag)
```  
```
HTB{why_d1d_1_s4v3_th3_fl4g_0n_th3_5t4ck?!}
```