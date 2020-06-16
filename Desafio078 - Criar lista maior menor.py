print(f"\033[;1m{'Desafio 78 - Criar lista, Maior - Menor':*^70}\033[m")
# Cria uma lista vazia
lista = []

# Preenche a lista vazia com valores e a quantidade escolhida.
for a in range (0, (int(input("Digite a quantidade máxima de valores: ")))):
    lista.append((int(input(f"Digite um valor para a posição {a}: "))))

# usando as funçoes max e min para achar os maiores e menores valores das listas
maior = max(lista)
menor = min(lista)

# Lista os menores valores
print(f"O menor valor na lista é o {menor} que está na posição: ", end='')
for p, v in enumerate(lista):
    if menor == v:
        print(f"{p}",end = "... ")

# Lista os maiores valores

print(f"\nO maior valor na lista é o {maior} que está na posição: ", end='')
for p, v in enumerate(lista):
    if maior == v:
        print(f"{p}", end = '... ')



