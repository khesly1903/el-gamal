import numpy as np
import math
import random
O = (np.inf,np.inf)

def ec_dis(a,b):
    discriminant = pow(4*a,3) + 27 * pow(b,2)
    if discriminant == 0:
        raise ValueError("Discriminant is 0")
     

def ec_point():
    pass

def inv(a,q):
    if a == q:
        raise ValueError("not invertible")
    elif a > q:
        a %= q
        return pow(a,-1,q)
    elif a < q:
        return pow(a,-1,q)
    else:
        raise ValueError("??nasi")
    

def is_on_curve(ec,q,P):
    a,b = ec
    x,y = P
    if pow(y,2,q) == pow(x,3,q) + a*x + b:
        pass
    else:
        raise ValueError

def negative(P):
    x_1,x_2 = P
    return x_1,-x_2

def addition(ec,q,P,Q):

    x_1,y_1 = P
    x_2,y_2 = Q

    a,b = ec
    
    if x_1 == np.inf and y_1 == np.inf: # O + P = P
        x_3,y_3 = x_2,y_2 

    elif x_2 == np.inf and y_2 == np.inf: # P + O = P
        x_3,y_3 = x_1,y_1
    
    elif (x_1 != x_2 and y_1 != y_2) or (x_1 != x_2 and y_1 == y_2): #point addition
        drv = ((y_2 - y_1) * inv(x_2-x_1,q)) %q
        x_3 = (pow(drv,2) - x_1 - x_2) %q
        y_3 = (drv * (x_1 - x_3) - y_1) %q

    elif x_1 == x_2 and y_1 == y_2: #point doubling
        drv = ((3*pow(x_1,2)+a)*(pow(2*y_1,-1,q))) %q
        x_3 = (pow(drv,2) - x_1 - x_2) %q
        y_3 = (drv * (x_1 - x_3) - y_1) %q

    elif x_1 == x_2 and (y_1 + y_2)%q == 0: #point negation
        x_3,y_3 = O

    

    
    R = x_3,y_3

    return R


def s_mult(ec,q, k, P): 
    R = P
    for i in range(1, k):
        R = addition(ec, q, P, R)
        
    return R

def order(ec,q,P):
    print(f"ORDER OF {P}")
    R = P
    order_of_point = 1
    while True:
        R = addition(ec, q, P, R)
        order_of_point += 1
        if R == O:
            break
    return order_of_point


def hasse_bound(q):
    hasse_lower = (-2)*math.sqrt(q)+q+1
    hasse_upper = 2*math.sqrt(q)+q+1
    print(f"Hasse bound for {q} is {hasse_lower} <= #E <= {hasse_upper}")


def encyption(ec,q,M,P,Q):
    k = random.randint(1, q - 1)
    print(f"random k = {k}")
    
    C_1 = s_mult(ec,q,k,P)

    C_2 = addition(ec,q,M,s_mult(ec,q,k,Q))



    return C_1,C_2
    
   

def decryption(ec,q,n,C_1,C_2):
    return addition(ec,q,C_2,negative(s_mult(ec,q,n,C_1)))


def main():
    a = int(input("a: "))
    b = int(input("b: "))
    ec = (a,b)
    q = int(input("q: "))

    x_0 , y_0 = input("P: ").split()
    x_0 = int(x_0)
    y_0 = int(y_0)
    P = x_0 , y_0


    n = int(input("secret n: ")) % q

    Q =  s_mult(ec,q,n,P)

    x_1 , y_1 = input("M(point): ").split()
    x_1 = int(x_1)
    y_1 = int(y_1)
    M = x_1 , y_1



    c_1,c_2 = encyption(ec,q,M,P,Q)
    print(f"Encrypted pair: {c_1},{c_2}")
    print(decryption(ec,q,n,c_1,c_2))
    

    
if __name__ == "__main__":
    main()
    

