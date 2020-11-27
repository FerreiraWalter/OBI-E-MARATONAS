#Álbum da Copa
N = int(input())
M = int(input())
album = []

for c in range(0, M):
  x = int(input())
  if x not in album:
    album.append(x)

restante = len(album)
total = N - restante
print(total)
