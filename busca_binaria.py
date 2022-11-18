def busca_binaria(lista, numero):
    # Retorna o índice do número na lista
    inicio = 0
    fim = len(lista) - 1 # Último índice da lista
    while inicio <= fim:  # Enquanto o início for menor ou igual ao fim

        meio = (inicio + fim) // 2  # Pega o meio da lista

        if lista[meio] == numero:  # Se o número estiver no meio da lista
            return meio  # Retorna o índice do meio da lista
        elif lista[meio] < numero:  # Se o número estiver antes do meio da lista
            inicio = meio + 1  # O início da lista passa a ser o meio + 1
        else:  # Se o número estiver depois do meio da lista
            fim = meio - 1  # O fim da lista passa a ser o meio - 1
    return None

def verifica(index):
    if index is not None:
        print(f"\nO número está na lista na posição: {index}\n")
    else:
        print("\nO número não está na lista\n")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = busca_binaria(lista, 10)
verifica(index)
