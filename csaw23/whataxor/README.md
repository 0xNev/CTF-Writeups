
# Whataxor
We are given a binary file and nothing else.
Lets run some checks on it.
  
```bash
file whataxor
```
```bash
pwn checksec whataxor
```
![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/1.png?raw=true)

Nothing out of the usual, now lets decomplile the binary in Ghidra.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/2.png?raw=true)


Taking a look at the main function, we see there are a bunch of variables being assigned.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/3.png?raw=true)


Scrolling down we see the programming is accepting a input then running the input through a function named 'xor_transform', then finally comparing the result with one of the earlier mentioned variables.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/4.png?raw=true)

Let's take a look at the xor transform function.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/5.png?raw=true)

It looks like a regular xor function, lets try extrating all the earlier mentioned variables then run them through xor with the key provided in the xor_transform function call.

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/6.png?raw=true)

That doesn't work, maybe convert from hex first?

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/whataxor/7.png?raw=true)

That looks like the flag!


