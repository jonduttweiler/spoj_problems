#python supports arbitrarily large integers naturally But still it does not (for now) supports an arbitrarily large float !!
n_test_cases = 10
for i in range(n_test_cases):
    a = int(input())
    b = int(input())
    #  operator // performs an integer division
    print(str((a+b)//2))
    print(str((a-b)//2))


