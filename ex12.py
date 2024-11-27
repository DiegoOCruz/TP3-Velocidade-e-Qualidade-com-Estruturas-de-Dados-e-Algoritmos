def soma_recursiva(lista):
    if not lista:
        return 0

    return lista[0] + soma_recursiva(lista[1:])

print(soma_recursiva([10,22,56,99,45,78,2365,1]))