def inserirInicio(lista, item):
  lista.insert(0, item)


def inserirFinal(lista, item):
  lista.append(item)


def removerInicio(lista):
  return lista.pop(0)


def removerFinal(lista):
  return lista.pop()


def tamanhoDeque(lista):
  return len(lista)


def palindromo(texto):
  lista = []

  for t in texto.lower():
    inserirFinal(lista, t)
  
  print(lista)
  palindromo = True

  cont = 0

  while (tamanhoDeque(lista) > 1 and palindromo):
    inicio = removerInicio(lista)
    print(cont ,'inicio', inicio)
    final = removerFinal(lista)
    print(cont, 'final', final)

    cont += 1

    if inicio != final:
      palindromo = False

  return palindromo



texto = "A rua Laura"
textoDois = "ovo"

texto = texto.replace(" ", "")

print(palindromo(texto))
