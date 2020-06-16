print(f"\033[;1m{'Desafio 079 - Criar uma lista sem repetições':*^70}\033[m")
lista = []
contador = 0

# Cria uma repetição para digitar varios valores na lista.
while True:
    numero = input("Informe o valor: " if contador == 0 else "Informe o valor ou ['N'] para sair: ")
    if numero.lower()[0] == 'n':
        break

    # Verifica se o numero esta na lista
    elif int(numero) in lista:
        print(f"\033[1;31mO valor {numero} já existe na posição {lista.index(int(numero))}\033[m")

    # Se o numero não existe ele é adicionado no final da lista.
    else:
        lista.append(int(numero))
        contador += 1
        print(f"\033[;34mValor {numero} adicionado com sucesso....\033[m")

lista.sort()
print(lista)