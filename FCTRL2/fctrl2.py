known_factorials= [None]*101
known_factorials[0] = 1

#parametrs int n
#returns n factorial, and if calculated another factorial, stores it at known_factorials
def factorial(n):
    if known_factorials[n] is not None:
        return known_factorials[n]
    else:
        known_factorials[n] = n * factorial(n - 1)
        return known_factorials[n]

n_test_cases = int(input())
for i in range(n_test_cases):
    print(str(factorial(int(input()))))



