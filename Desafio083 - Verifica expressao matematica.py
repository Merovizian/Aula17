print(f"\033[;1m{'Desafio 083 - Verifica a integridade de uma expressão':*^70}\033[m")
# Usuaria digita a expressão
expressao = input("Digite a expressão: ")
# transforma a str digitada em uma lista
lista = list(expressao)
# auxiliares que vão fazer a contagem dos parenteses
aberto = lista.count('(')
fechado = lista.count(')')


# se a soma de abertos e fechados for divergente
if aberto != fechado:
    print("\033[1;31mHá um erro na sua expressão!")
    if aberto > fechado:
        print("\033[1;33mHá um parentêses que não foi fechado")
    else:
        print("\033[1;33mHá um que não foi aberto")
# se a soma de abertos e fechados for igual
else:
    print("\033[1;34mSua Expressão está correta!")