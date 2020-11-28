#ENTRADA DE DASDOS:

A = int(input())
B = int(input())
C = int(input())

caixa = [A, B, C]
caixa.sort()

H = int(input())
L = int(input())

janela = [H, L]
janela.sort()

#PROCESSAMENTO:

if caixa[0] <= janela[0] and caixa[1] <= janela[1]:
    print('S')
else:
    print('N')