
def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial_recursivo(n - 1)

contador = 999
while True:
    try:
        print(f'Fatorial de {contador}:')
        print(fatorial_recursivo(contador))
        contador += 1
    except RecursionError:
        print(f'Stack Overflow: o limite de recursão foi atingido.')
        break

print('\n')
print('Fatorial Iterativo:')
def fatorial_iterativo(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

contador = 999
while contador != 1001:
    try:
        print(f'Fatorial de {contador}:')
        print(fatorial_iterativo(contador))
        contador += 1
    except RecursionError:
        print(f'Stack Overflow: o limite de recursão foi atingido.')
        break
    except OverflowError:
        print(f'Overflow: o resultado é muito grande para ser armazenado.')
        break