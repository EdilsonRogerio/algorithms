def busca_linear(lista, numero):
    # Retorna o índice do número na lista
    for i in range(len(lista)): # Percorre a lista
        if lista[i] == numero: # Se o número estiver na lista
            return i # Retorna o índice do número
    return None

def verifica(index):
    if index is not None:
        print(f"\nO número está na lista na posição:{index}\n")
    else:
        print("\nO número não está na lista\n")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = busca_linear(lista, 4)
verifica(index)