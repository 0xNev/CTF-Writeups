
# BabysThird
We are given a binary file and nothing else.
Lets run some checks on it.
  
```bash
file babys_third
```
```bash
pwn checksec babys_third
```

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/babysthird/1.png?raw=true)


Nothing out of the usual, now lets decomplile the binary in Ghidra.

Taking a look at the main function, the flag is in plain sight!

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/babysthird/2.png?raw=true)

