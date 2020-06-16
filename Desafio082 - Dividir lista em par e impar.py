print(f"\033[;1m{'Desafio 082 - Dividir uma lista em 2 listas par e impar':*^70}\033[m")
# São criadas 3 listas separadamente, pois se não elas ficam interligadas
lista = []
listaPAR = []
listaIMPAR = []
# Loop para a criação de lista
while True:
    numero = input("Insira um valor: " if lista == [] else "Insira um valor ['N' para sair]: ")
    if numero.lower()[0] == 'n':
        break
    lista.append(int(numero))
# laço que percorre toda a lista e separa os numeros pares e impares, colocando em suas respectivas listas
for a in lista:
    if a % 2 == 0:
        listaPAR.append(a)
    else:
        listaIMPAR.append(a)

print('-='*30)
print("Lista Original:",lista,"\nLista PAR:",listaPAR,"\nLista IMPAR:",listaIMPAR)
print('-='*30)