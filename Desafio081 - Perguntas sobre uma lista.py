print(f"\033[;1m{'Desafio 081 - Trabalhando uma lista':*^70}\033[m")
lista = []
contador = escolha = 0
# Loop para criar uma lista
while True:
    numero = input("Insira um valor: " if contador == 0 else "Insira um valor ['N' para sair]: ")
    if numero.lower()[0] == 'n':
        break
    lista.append(int(numero))
    contador += 1

# Loop para fazer o menu
while True:
    print('-='*30)
    print(f"{'LISTA':^60}\n{str(lista):^60}")
    escolha = input(f"Escolha uma opção\n1 - Quantos números foram digitados.\n2 - Lista Crescente\n3 - Lista Decrescente\n4 - Procurar um valor na lista\n0 - Sair\nEscolha: ")

    if escolha == '0':
        break
    if escolha == '1':
        print(f"A lista {lista} tem {len(lista)} numeros")
        input("Digite Enter para continuar ...")
    # Criei uma lista paralela para nao afetar a primeira
    if escolha == '2':
        listaB = lista[:]
        listaB.sort()
        print(f"{lista} ordenada de forma crescente {listaB}")
        input("Digite Enter para continuar ...")

    # Criei uma lista paralela para nao afetar a primeira
    if escolha == '3':
        listaB = lista[:]
        listaB.sort(reverse=True)
        print(f"{lista} ordenada de forma decrescente {listaB}")
        input("Digite Enter para continuar ...")

    if escolha == '4':
        valor = int(input("Informe o valor para procurar na lista: "))
        # Verifica se existe o valor primeiro
        if valor in lista:
            # se o valor existe procura a posição dele
            for p, v in enumerate(lista):
                if valor == v:
                    print(f"O valor {valor} esta na posição {p} da lista {lista}")
        else:
            print(f"O valor {valor} não está em {lista}")
        input("Digite Enter para continuar ...")
