# Mod

- Description: Just a simple modulo challenge

- Author: NoobMaster

# Solution

### Observations

```
#!/usr/local/bin/python3
import os
secret = int(os.urandom(32).hex(),16)
print("Welcome to Mod!")
num=int(input("Provide a number: "))
print(num % secret)
guess = int(input("Guess: "))
if guess==secret:
    print(open('flag.txt').read())
else:
    print("Incorrect!")
```

Here, we have a $128$-bit number that we have to guess to get the `flag.txt`. 

The only information we obtain is by providing a `num` as input and getting `num` mod `secret` as the `output`.

The issue with this is for every `output` we get, we can have multiple possibilities for `secret` even if we know `num`.

### Approach 1

We can just blindly brute force it by guessing `secret` = `num` - `output` and eventually we'll guess it correctly as there are very few possibilities for `secret` and we'll eventually guess the right `secret`.

But this is too much work.

### Key Observation

The input can take negative numbers too. The challenge allows us to do it.

Now, we know that $-1$ mod `secret` $=$ `secret` $- 1$.

This is the key observation we had to find. Now the approach is pretty simple

### Final Approach

We give $-1$ as the input and we will receive `secret` $- 1$ as the `output`.

Then we guess `output` $+ 1$ to recieve the flag.

The flag recieved confirms that this was the intended solution

# Flag

flag = n00bz{-1_f0r_7h3_w1n_4a3f7db1}
