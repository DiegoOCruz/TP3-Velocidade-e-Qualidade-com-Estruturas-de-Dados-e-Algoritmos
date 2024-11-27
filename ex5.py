def quicksort(array):
    # Caso base: se o array tiver 1 ou nenhum elemento, ele já está ordenado
    if len(array) <= 1:
        return array

    # Escolhe o pivô (neste caso, o último elemento da lista)
    pivot = array[-1]

    # Particiona o array em sub-arrays de elementos menores, iguais e maiores que o pivô
    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]

    # Chama o quicksort recursivamente e concatena os resultados
    return quicksort(menores) + [pivot] + quicksort(maiores)

# Exemplo de uso
array = [10, 7, 8, 9, 1, 5]
ordenado = quicksort(array)
print("Array ordenado:", ordenado)
