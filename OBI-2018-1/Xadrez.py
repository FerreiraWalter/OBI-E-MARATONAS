#Xadrez
L = int(input())
C = int(input())

if (L % 2 == 0 and C % 2 == 0) or (L % 2 != 0 and C % 2 != 0):
  print('1')
else:
  print('0')