
# You know 0xDiablos
We are given a nc command and the bianry.
```bash
nc <someip> <someport>
```
The program is asking for an input

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/1.png?raw=true)

Let's do some checks

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/2.png?raw=true)

Plenty of possibilities.

Let's decomplie the binary in Ghidra.

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/3.png?raw=true)


Here's main, looks like main's only purpose is to print some text then call the function 'vuln'. Lets look at that function.

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/4.png?raw=true)

The function is using gets() to grab an input then printing the input. Since gets() is being used we'll be doing a buffer overflow. Lets see if there's a useful function we could return to.

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/5.png?raw=true)

There's a flag function which will open and print the flag. The only problem is the function takes in 2 arguments, and checking their values before printing the flag. We'll need to be sure to emulate these variables in our payload.

First we'll overwrite the return address to the flag function pointer, we then  will also need to add the other two arguments to the stack.

Since this binary is 32 bit the arguments are stored on stack, meaning we'll be able to set the arguments  in our initial payload to jump to the flag function.

We'll then need to find the offset  so we can decide where to start our payload. I found this with pwn cyclic.

Now we'll execute our payload.

![](https://github.com/0xNev/CTF-Writeups/blob/main/htb/0xdiablos/6.png?raw=true)

```bash
HTB{0ur_Buff3r_1s_not_healthy}
```