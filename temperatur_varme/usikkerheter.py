import numpy as np

def usikker_add(delta_A, delta_B):
    delta_Zadd = np.sqrt(delta_A**2 + delta_B**2)
    return delta_Zadd

def usikker_pow(n, A, delta_A, Z):
    delta_Zpow = Z*n*(delta_A/A)
    return delta_Zpow

def usikker_ln(A, delta_A):
    delta_Zln = delta_A/A
    return delta_Zln


first_step = usikker_add(0.2, 0.1)
second_step = usikker_ln(
