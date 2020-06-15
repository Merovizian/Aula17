# Listas são mutáveis, juntados por []
lista = [0, '1', 'L', 'B', 9, 0, 'l']

# lista.append({objeto}) - adiciona um valor na ultima posição da lista.
lista.append('A')

# lista.insert({posição},{objeto}) - Insere um objeto na opção informada.
lista.insert(1, 'B')

# del lista[] - remove o objeto da posição
del lista[2]

# lista.pop() - remove o objeto da posição , se não colocar a posição ele remove o ultimo
lista.pop(1)

# lista.remove({objeto}) - remove o primeiro objeto desejado da lista. Se não estiver na lista, ele retorna erro.
lista.remove('A')

# lista = list(range(valor1,valor2,passo)) - cria uma lista com o intervalo dado.
lista = list(range(0, 19, 2))

# lista.sort() - Organiza em ordem alfabetica e lista.sort(reverse=True) Organiza de forma contrária.
lista.sort()
lista.sort(reverse=True)
lista.reverse()

# for a , b in enumerate(lista).  'a' - posição e 'b' o valor.
for a, b in enumerate(lista):
    print(a,b)

# listaA = listaB - Cria-se uma ligação entre as duas, mudando-se A muda-se B.
listaB = lista
listaB[0] = 'A'

# listaA = listaB[:] - Cria-se uma cópia de todos os elementos de B em A, sem criar uma ligação.
listaA = listaB[:]
listaA[0] = 'KK'
print(listaB)
print(listaA)