import math
import multiprocessing
import time
import numpy as np
import random

def check_prime(num, verbose=False):
    t1 = time.time()
    res = False
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                if verbose:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    print("Time:", int(time.time()-t1))
                break
        else:
            if verbose:
                print(num,"is a prime number")
                print("Time:", time.time()-t1) 
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res

def check_prime_list(data, verbose=False):
    for i in data:
        check_prime(i, verbose)

def pi_monte_carlo(n):
    count = 0
    radius = 1

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if math.sqrt(x**2 + y**2) < radius**2:
            count += 1

    return count

def pi_bbp(k):
    term = 1/16**k * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    return term

def calculate_pct_changes(data):
    pct_changes = [np.nan]
    for x1, x2 in zip(data[:-1], data[1:]):
        pct = (x2 - x1) * 100 / x1
        pct_changes.append(pct)
    return pct_changes
