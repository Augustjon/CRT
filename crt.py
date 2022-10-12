from logging import raiseExceptions
from math import gcd
import itertools
import numpy as np

def main():
    a_i = []
    m_i = []
    M_i = []
    b_i = []
  
    
    f = open("problem.txt", "r")
    line = f.readline()
    while line:
        input = line.split(" ")
        a_i.append(int(input[0]))
        m_i.append(int(input[1]))        
        line = f.readline()
    f.close() 

    k = len(a_i)
    m =  np.prod(m_i)

    if k < 2:
        print("the Problem must be a system of at least two equations")

    pairs = itertools.combinations(m_i, 2)
    for x in pairs:
        if not(is_coprime(x[0], x[1])):
            raise Exception("The modules are not pairwise reletively prime")

    for i in range(len(m_i)):
        M_i.append(np.prod(m_i)/m_i[i])
    
    for i in range(0, len(M_i)):
        b_i.append(find_mod_inverse(M_i[i], m_i[i]))

    ## solution to the system is x = a1*M1*b1 + .... + ak*Mk*bk mod m
    x = 0
    for i in range(1, k):
        x = x + a_i[i]*M_i[i]*b_i[i]
    x = x%m

    print("the solution to the system is: " + str(x) + " mod " + str(m))    



def find_mod_inverse(a,m):
    for x in range(1,m):
        if ((a%m)*(x%m) % m==1):
            return x
    raise Exception('modular inverse does not exist')            

def is_coprime(a, b):
    return gcd(a, b) == 1

if __name__ == "__main__":
    main()    




