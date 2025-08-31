#!/usr/bin/env python3
from pwn import *

#Connecting to the remote connection
r = remote('play.scriptsorcerers.xyz', 10166)

#Set the inital range
low = 1 << 127
high = 1 << 128 - 1      

#Loop until the we find the number (low == high)
while low < high:
	mid = (low + high) // 2 + 1
	
	#Choose Option 1 to perform the binary search
	r.sendlineafter(b"Choice: ", b"1")
            
	# Send our number 
	r.sendlineafter(b"Enter a number: ", str(mid).encode())
            
        # Get the output
        output = r.recvline().strip()
        div = int(result_line)

        #If div is 0, the number is in lower half and if div is 1 then number is upper half
        if div == 0:
		high = mid
        else: # R is 1 or greater
                low = mid + 1

#The secret has been found
secret = low


#Submit the secret to get the flag
r.sendlineafter(b"Choice: ", b"2")
r.sendlineafter(b"Enter secret number: ", str(secret).encode())

#Receive and print the flag
flag = r.recvall(timeout=2).strip().decode()
log.success(f"FLAG: {flag}")