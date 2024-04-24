from math import gcd
import random

def is_prime(p):
    if p > 1:
        for i in range(2, (p//2)+1):    
            if (p % i) == 0:
                raise ValueError(f"{p} is not a prime number")
        else:
            True
    else:
        raise ValueError(f"{p} must be positive integer")

def is_coprime(a, b):
    if gcd(a,b) != 1:
        raise ValueError(f"{a} and {b} are not relatively prime. ")
    else:
        pass

def order(g, p):
    order = 1
    while True:
        if pow(g, order, p) == 1:
            return order
        order += 1


def encryption(g,p,A,m):
    k = random.randint(1,p-1)
    c_1 = pow(g,k,p) 
    c_2 = (m*pow(A,k,p)) %p
    print(f"Random key: {k}")
    return c_1,c_2

def decryption(c_1,c_2,a,p):
    return pow(pow(c_1,a),-1,p)*c_2 % p

def main():
    p = int(input("p: "))
    is_prime(p)
    
    g = int(input("g: "))
    

    ord = order(g,p)
    
    if ord == p-1: #?
        pass
    elif is_prime(ord) == True:
        pass
    else:
        raise ValueError(f"{g} has not prime order")


    a = int(input("Alice`s private key: "))
    a = a%p
    A = pow(g,a,p)
    m = int(input("Message: "))

    c_1,c_2 = encryption(g,p,A,m)

    
    print(f"Encrypted message: ({c_1},{c_2})")
    print(f"Decrypted message: {decryption(c_1,c_2,a,p)}")

if __name__ == "__main__":
    main()
