n = int(input())
d = int(input())
a = int(input())

if a == d:
    print('0')
elif a < d:
    print('{}'.format(d - a))
elif a > d:
    print('{}'.format((n - a) + 1 + (d - 1)))