def contar_repeticoes(string, letra):
    if len(string) == 0:
        return 0
    if string[0] == letra:
        return 1 + contar_repeticoes(string[1:], letra)
    else:
        return contar_repeticoes(string[1:], letra)
    
print(contar_repeticoes("banana", "a")) 