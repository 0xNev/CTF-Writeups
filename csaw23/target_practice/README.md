# Target Practice
We are given a netcat command.
```bash
nc intro.csaw.io 31138
```
Here's a look at the output.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/target_practice/1.png?raw=true)

We were also given the binary, lets run some checks on it
```bash
file target_practice
```
```bash
pwn checksec target_practice
```
![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/target_practice/2.png?raw=true)

Nothing out of the ordinary, now lets decomplile the binary in Ghidra.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/target_practice/3.png?raw=true)

Taking a look at the main function, we see that the program is taking an input then making a function call to the referenced input. Lets see if we can find a useful function to jump to.
Taking a closer look, we find a function named 'cat_flag'

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/target_practice/4.png?raw=true)

The function makes a syscall which will print the flag, this is exactly what we need. We'll copy the address to the function then use that as our input. Here's the address to the 'cat_flag' function - '00400717'

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/target_practice/5.png?raw=true)