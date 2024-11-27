
def palindromo(palavra):
    if len(palavra) <= 1:
        return True
    if palavra[0] != palavra[-1]:
        return False
    return palindromo(palavra[1:-1])

print(palindromo('Gato'))
print(palindromo('ovo'))