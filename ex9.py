class Node:
    def __init__(self, value):
        self.value = value
        self.esquerda = None
        self.direita = None

def in_order_traversal(node):
    if node is None:
        return []
    # Visita o lado esquerdo, o nó atual e o lado direito
    return in_order_traversal(node.esquerda) + [node.value] + in_order_traversal(node.direita)

# Criando a árvore
root = Node(100)
root.esquerda = Node(53)
root.direita = Node(5)
root.esquerda.esquerda = Node(13)
root.esquerda.direita = Node(67)
root.direita.esquerda = Node(22)
root.direita.direita = Node(8)

# Percorrendo a árvore em ordem
result = in_order_traversal(root)
print(result)
