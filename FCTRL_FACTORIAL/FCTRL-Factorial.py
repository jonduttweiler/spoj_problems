import math
#def z(n):
#    n_string = str(math.factorial(n))
#    i_end = len(n_string.rstrip('0'))
#    return len(n_string[i_end:])

def z2(n):
    pot = 1   # 1,2,3,4,5,..
    res = 0
    c_pow = 5

    while c_pow <= n:
        res += math.floor(n/c_pow)
        pot += 1
        c_pow = 5 * c_pow

    return int(res)

n_test_cases = int(input())
for i in range(n_test_cases):
    print(str(z2(int(input()))))