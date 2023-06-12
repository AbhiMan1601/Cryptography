############################################
# RSA CTF Generator 
# Credits go to Prof Bill Buchanan 
# who put it up on Medium as a self starter to solve
# CTFs on RSA encryption scheme
############################################

# writing imports 
# crypto util is used to generate ciphers
# sympy is used for symbolic mathematics (basically to generate random primes)
from Crypto.Util.number import long_to_bytes,bytes_to_long
from Crypto import Random
import Crypto
import sympy
import math

# Initializing variables
# e is taken as 65537
bits=256
e=65537
msg="Hello"

# We need to find d

# bruteforcing for the values of d
# the main problem here is figuring out values of N 
# it will be given that one of the primes (say p) will be small
badprime=sympy.randprime(0, 10000)
m=  bytes_to_long(msg.encode())
q=sympy.randprime(0, 10000)
p = Crypto.Util.number.getPrime(bits-int(math.log10(badprime)//math.log10(2)), randfunc=Crypto.Random.get_random_bytes)
N=p*q

# CTF problem generator
C=pow(m,e,N)
print(f"Bob sends Alice a cipher using the RSA method. The cipher is {C} and the public modulus is {N}. The value of e is {e}. Unfortunately a low factor has been used to generate N.\nUsing this information, can you crack the cipher, and find the message?")
print("\n\nAnswer:") # Bruteforcing for value of d
for p in sympy.primerange(0, 10000):
 if (N%p==0): 
  q=N//p
  print(f"Found at {p} and {q}")
  PHI=(p-1)*(q-1)
  print(f"PHI={PHI}")
  d=pow(e,-1,PHI)
  m=pow(C,d,N)
  print(f"\nDecipher: {long_to_bytes(m).decode()}")
  break

print(f"\nTo check, the values used are:")
print("p=",p)
print("q=",q)