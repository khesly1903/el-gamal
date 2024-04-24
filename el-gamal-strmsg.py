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

def int_message(msg):
    int_msg = []
    for char in msg:
        int_msg.append(ord(char))
    return int_msg

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

def encryption(g, p, A, int_msg):
    k = random.randint(1, p - 1)
    print("Empheral random key: ", k)
    enc_msg = []
    for m in int_msg:
        m = (m * pow(A, k, p)) % p
        enc_msg.append(m)
    c_1 = pow(g, k, p)
    c_2 = enc_msg
    return c_1, c_2

def decryption(a,p,c_1,c_2):
    dec_msg = []
    for d_msg in c_2:
        m = (pow(c_1,-a,p)*d_msg)%p
        dec_msg.append(m)
    return dec_msg
    


def main():


    #Large prime p
    p = int(input("p: "))
    is_prime(p)

    #Primitive element g with large prime order
    g = int(input("g: "))
    
    #Find the order of g and check that it is prime or not
    order_g = order(g,p)

    if order_g == p-1: #it generates the whole group
        pass
    elif is_prime(order_g) == True: #prime case
        pass
    else: #composite order case
        raise ValueError(f"{g} has not prime order, order is {order(g,p)}")
    
    #Take the A`s private key modulo p
    a = int(input("Alice`s private key: ")) %p

    #Calculate the public key
    A= pow(g,a,p)


    #Bob chooses message
    msg = str(input("String message: "))
    
    #Convert string to int ascii
    int_msg = []
    int_msg = int_message(msg)

    print(f"ASCII: {int_msg}")
    
    #Encrypt the plaintext
    c_1,c_2 = encryption(g,p,A,int_msg)

    print(f"Encrypted pair: c_1: {c_1}, c_2: {c_2}")

    #Decrypt the plaintext
    m = decryption(a,p,c_1,c_2)

    print(f"Decrypted: {m}")



if __name__ == "__main__":
    main()
    

