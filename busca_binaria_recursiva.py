def busca_binaria_recursiva(lista, numero):
    if len(lista) == 0:  # Se a lista estiver vazia retorna None
        return False
    else:

        meio = len(lista) // 2  # Pega o meio da lista

        if lista[meio] == numero:  # Se o número estiver no meio da lista
            return True  # Retorna True
        else:
            if lista[meio] < numero:  # Se o número estiver depois do meio da lista
                metade_a_direita = lista[meio + 1:]
                # Retorna a busca binária recursiva da metade a direita da lista
                return busca_binaria_recursiva(metade_a_direita, numero)
            else:  # Se o número estiver antes do meio da lista
                metade_a_esquerda = lista[:meio]
                # Retorna a busca binária recursiva da metade a esquerda da lista
                return busca_binaria_recursiva(metade_a_esquerda, numero)


def verifica(index):
    print(f"Número encotrado: {index}")


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = busca_binaria_recursiva(lista, 10)
verifica(index)

index = busca_binaria_recursiva(lista, 30)
verifica(index)
