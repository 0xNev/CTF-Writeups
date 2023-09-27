# Target Practice

The challange provides us with a ELF binary and a nc command

We can assume that the nc server is running the binary we are provided, to be sure of this we can do a quick check on both

By running 'nc intro.csaw.io 31138' in our terminal we receive the following message


We see the program is expecting an input, let's try something random


After sending the input the connection closes


Lets take a look at the binary we were given, I first ran strings to see if we could get anything useful


Not much, other than 'cat flag' but that's not really useful

We'll take a deeper look with ghidra

Here is the main function decompiled from ghidra




The program is taking our input and storing it to the local_20 varible. Looking a few lines past that we see the program is referincing our input as a pointer then making a function call too the pointer. Knowing this if we can find a useful function in the code we might be able to call it. 

Further analysis of the binary I found the function which ghidra decompiled named 'cat_flag'. Here is what the function looks like.

void cat_flag(void)
{
    system("cat /flag.txt");
    return;

}

The function makes a sys call to print the flag. This is exactly what we needed. We can go ahead amd copy the address to the function and try it as our input. 







