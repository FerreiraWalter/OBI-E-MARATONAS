#Escadinha
N = int(input())

num = input().split()
for i in range(len(num)):
  num[i] = int(num[i])

resp = 1
i = 2
while i < len(num):
  if (num[i] - num[i-1]) != (num[i-1] - num[i-2]):
    resp += 1
  i += 1

print(resp)