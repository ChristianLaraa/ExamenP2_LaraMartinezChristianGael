# Examen Practico - Lara Martinez Christian Gael
# Representa un nodo de árbol rojo-negro
class Node:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    # Insertar un valor en el árbol
    def insert(self, value):
        self.root = self._insert(self.root, value)

    # Inserta un valor en el árbol de manera recursiva
    def _insert(self, node, value):
        if node is None:
            return Node(value, "black")

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:
            return node

        # Balancea el árbol
        self._balance(node)

        return node

    
    def _balance(self, node):
        while node is not None:
           
            if node.color == "red" and node.left.color == "red" and node.right.color == "red":
                self._rotate(node)
                node.color = "black"
                node.left.color = "black"
                node.right.color = "black"

           
            if node.color == "red" and node.left.color == "red" and node.right.color == "black":
                self._left_rotate(node)
                node.color = "black"
                node.left.color = "red"

            if node.color == "red" and node.left.color == "black" and node.right.color == "red":
                self._right_rotate(node)
                node.color = "black"
                node.right.color = "red"

            node = node.parent

    # Rota el árbol a la izquierda
    def _left_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node

        right.parent = node.parent
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = right
            else:
                node.parent.right = right

        node.parent = right

    # Rota el árbol a la derecha
    def _right_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node

        left.parent = node.parent
        if node.parent is not None:
            if node == node.parent.left:
                node.parent.left = left
            else:
                node.parent.right = left

        node.parent = left

# Crea el árbol
tree = RedBlackTree()

# Inserta los valores en el árbol
tree.insert(26)
tree.insert(64)
tree.insert(6)
tree.insert(28)
tree.insert(53)
tree.insert(84)
tree.insert(9)
tree.insert(37)
tree.insert(56)
tree.insert(75)
tree.insert(90)


tree.insert(62)

print(tree)
