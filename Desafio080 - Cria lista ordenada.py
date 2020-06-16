print(f"\033[;1m{'Desafio 080 - Criar lista Ordenada':*^70}\033[m")
contador = aux = 0
lista =[]

# Loop para criar uma lista
while True:
    numero = input("Digite um valor: " if contador == 0 else "Digite um valor ou [N] para sair: " )
    if numero.lower()[0] == 'n':
        break

    else:
        #  Loop que Roda toda a lista
        for p, v in enumerate(lista):
            # Procura na lista um numero maior, e se achar, o numero informado é colocado antes dele.
            if int(numero) <= v:
                lista.insert(p,int(numero))
                print(f"O valor {numero} foi adicionado na posição {p} da lista\n{lista}")
                aux = 1
                break
    # Se não achar um numero maior o numero dado é colocado por ultimo
    if contador == 0 or aux == 0:
        lista.append(int(numero))
        print(f"O valor {numero} foi adicionado no final da lista\n{lista}")

    contador += 1
    aux = 0

'''print(f"O valor {numero} foi adicionado na posição {p} da lista\n{lista}")
'''
