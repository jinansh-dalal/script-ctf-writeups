# Subtract

- Description : The image size is 500x500. You might want to remove some stuff...

- Author : NoobMaster

# Solution

### Observations

We have a very large text file. On analysing it, we find that there are $250,573$ co-ordinates in the text file. But there can be only $250,000$ unique co-ordinates in a $500 \times 500$ image.

Now, the description gives us an hint that we have to remove some stuff.

The stuff that has to be removed can be these duplicate co-ordinates. Maybe?

But, how can we remove these co-ordinates?

### Approach

Let's set these co-ordinates in the picture to be black. Hence, removing them.

Doing this does the trick and we get the flag.

The script used is ./solve_Subtract.py

# Flag

flag - scriptCTF{5ub7r4c7_7h3_n01s3}
