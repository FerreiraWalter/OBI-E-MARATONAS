C = int(input())
A = int(input())

if A % (C - 1) == 0:
    print(A // (C - 1))
else:
    print((A // (C - 1)) + 1)