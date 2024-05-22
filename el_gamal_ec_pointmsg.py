import numpy as np
import random
import ec_overF_lib as ecf

def center_text(message, width=80):
    lines = message.strip().split('\n')
    centered_lines = [line.center(width) for line in lines]    
    centered_message = '\n'.join(centered_lines)
    
    return centered_message

def encyption(ec,q,k,M,P,Q):
    
    C_1 = ecf.double_and_add(ec,q,k,P)
    C_2 = ecf.addition(ec,q,M,ecf.double_and_add(ec,q,k,Q))
    
    return C_1,C_2
    
   

def decryption(ec,q,n,C_1,C_2):
    return ecf.addition(ec,q,C_2,ecf.negative(ecf.double_and_add(ec,q,n,C_1)))


def main():
    
    print(center_text("""
Decide a large prime q, 
an elliptic curve E over F_p
and a point P in E(F_p)
          """))
    
    q = int(input("q: "))
    
    print(center_text("""
To construct an elliptic curve over a finite field, 
please provide the parameters a and b for the equation 
y^2 = x^3 + ax + b
          """))
    a = int(input("a: "))
    b = int(input("b: "))
    ec = (a,b)

    
    # a = 12
    # b = 45
    # ec = (a,b)
    # q = 983
    
        
    print(center_text("""
Give a point in E(F_p)
          """))


    x_0 , y_0 = input("P: ").split()
    x_0 = int(x_0)
    y_0 = int(y_0)
    P = x_0 , y_0
    
    ecf.is_on_curve(ec,q,P)

    print(center_text(("""
Alice chooses a secret n in Z
          """)))

    n = int(input("n: ")) 

    Q =  ecf.double_and_add(ec,q,n,P)
    
    print(center_text((f"""
Alice computes the point:
n x P = Q  
{n} x {P} = {Q} 
and sends to Bob as public key
          """)))


    print(center_text(("""
Bob chooses plaintext M in E(F_p)
          """)))
    x_1 , y_1 = input("M: ").split()
    x_1 = int(x_1)
    y_1 = int(y_1)
    M = x_1 , y_1

    ecf.is_on_curve(ec,q,M)
    
    k = random.randint(1, q - 1)
        
    print(center_text((f"""
Bob chooses a random key k = {k} in Z
          """)))
    c_1,c_2 = encyption(ec,q,k,M,P,Q)
    
    print(center_text((f"""
Bob uses Alice's public key Q to compute
C_1 = k x P
{c_1} = {k} x {P}

C_2 = M + kQ
{c_2} = {M} + {k}{Q}
          """)))

    M = decryption(ec,q,n,c_1,c_2)
    print(center_text(f"""
Alice computes the message M:
M = C_2 - nC_1
{M} = {c_2} - {n}{c_1}
          """))

    

    
if __name__ == "__main__":
    main()
    

