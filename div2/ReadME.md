# Div2 

- Description: Some might call this a programming challenge...

- Author: NoobMaster

# Solution

### Observations
The `secret` number to be guessed is a 128 bit number because we are adding $2^{127}$ to a random number between $1$ and $2^{127}$, which means that `secret` has to be in the interval $[2^{127} + 1, 2^{128}]$.
```
secret =  secrets.randbelow(1 << 127) + (1 << 127)
```

Now, the challenge gives us $2$ options every time.

The first option is to give an input and then recieve some output based on it.

The second option is to guess the `secret` and it will output the flag.

So, first we need to find the `secret` using the first option and then guess it using the second option to recieve the flag.

### Finding `secret`

```
num = input('Enter a number: ')
        fl_num = decimal.Decimal(num)
        assert int(fl_num).bit_length() == secret.bit_length()
        div = secret / fl_num
        print(int(div))
```
We can guess a number and it will return the value of `secret`/`f1_num`. But, there are some restrictions on what `f1_num` we can give. `f1_num` has to be a $128$-bit number as `secret` is also a $128$ bit number. So, the interval in which we can give an input from is $[2^{127} + 1, 2^{128}]$.

Due to these restrictions and since we are getting the integer value of `div`, `div` can have only $2$ values - $0$ or $1$. It will take the value $0$ when `secret` $<$ `f1_num` and $1$ when `secret` $\geq$ `f1_num`.

By giving such inputs, we can gradually reduce the search space based on if `div` is $0$ or $1$.

But the challenge only allows us to do this $1000$ times. And our interval size is $2^{127}$. So by using binary search, in the worst-case, we'll narrow down the interval in $\log_2(2^{127}) = 127$ guesses.

### Recieving the `flag`

```
guess = int(input("Enter secret number: "))
        if guess == secret:
            print(open('flag.txt').read().strip())
        else:
            print("Incorrect!")
        exit(0)
```
Now, we can just guess `secret` and recieve the flag.

# Approach

We can obviously take the brute force approach and manually find the number but we are not losers. We'll write a script to do that for us.

The script is pretty self-explanatory and in ./solve_div2.py

# Flag

Flag = scriptCTF{b1n4ry_s34rch_u51ng_d1v1s10n?!!}
