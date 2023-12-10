class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        def __str__(self):
            return str(self.value)
        
    # adiciona um nó na arvore
    def _add_branch(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left._add_branch(value)
        elif value > self.value:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right._add_branch(value)

    # printa a arvore
    def _print_tree(self, space=0):
        if self.right:
            self.right._print_tree(space + 2)
        print(" " * space, str(self.value))
        if self.left:
            self.left._print_tree(space + 2)

    def print_postorder(self):
        if self.left:
            self.left.print_postorder()
        if self.right:
            self.right.print_postorder()
        print(self.value)

    # encontra um nó e retorna o mesmo
    def _find_branch(self, value):
        if self is None or self.value == value:
            return self
        elif value < self.value:
            return self.left._find_branch(value)
        else:
            return self.right._find_branch(value)

    # encontra o menor nó de uma arvore
    def find_min(self):
        if self is None:
            return self
        elif self.left is not None:
            return self.left.find_min()
        return self
    
    # encontra o maior nó de uma estrutura de arvore
    def find_max(self):
        if self is None:
            return self
        elif self.right is not None:
            return self.right.find_max()
        return self

    def _cut_root(self):
        if self.left is None and self.right is None:
            return None
        if self.left is None:
                temp = self.right
                self = None
                return temp
        elif self.right is None:
            temp = self.left
            self = None
            return temp
        temp = self.right.find_min()
        self.value = temp.value
        self.right = self.right.remove(temp.value)
        return self
    
    def remove(self, value):
        if self is None:
            return self

        # Se o valor a ser removido é menor que o valor do nó, então está na subárvore à esquerda
        if value < self.value:
            if self.left:
                self.left = self.left.remove(value)
        # Se o valor a ser removido é maior que o valor do nó, então está na subárvore à direita
        elif value > self.value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            # Caso com apenas um filho ou sem filhos
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp

            # Caso com dois filhos, o nó será substituído pelo nó in-order sucessor (menor na subárvore à direita)
            temp = self.right.find_min()
            self.value = temp.value
            # Remova o in-order sucessor
            self.right = self.right.remove(temp.value)

        return self

    def find_height(self, node=None):
        h_left = 0
        h_right = 0
        if self.left:
            h_left = self.left.find_height(self.left)
        if self.right:
            h_right = self.right.find_height(self.right)
        if h_right > h_left:
            return h_right + 1
        return h_left + 1
    
class Tree:
    def __init__(self):
        self.root = None

    def add_branch(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root._add_branch(value)
    
    def print_tree(self):
        if self.root is not None:
            self.root._print_tree()
        else:
            print("Empty tree")

    def find_branch(self, value):
        if self.root is None:
            return None
        else:
            return self.root._find_branch(value)

    def cut_root(self):
        if self.root is None:
            return self.root
        else:
            self.root = self.root._cut_root()
    
    def remove(self, value):
        if self.root is not None:
            self.root = self.root.remove(value)


if __name__ == "__main__":
    tree = Tree()
    tree.add_branch(4)
    tree.add_branch(6)
    # tree.add_branch(5)
    # tree.add_branch(2)
    # tree.add_branch(3)
    # tree.add_branch(1)
    # tree.add_branch(0)
    # tree.add_branch(11)
    # tree.add_branch(-2)
    # tree.add_branch(10)
    # tree.add_branch(-1)
    # tree.add_branch(9)
    # tree.add_branch(7)
    # tree.add_branch(8)
    # tree.add_branch(12)
    # tree.add_branch(13)

    tree.print_tree()
    tree.cut_root()
    print("---")
    tree.print_tree()
    # node_to_remove = tree.find_branch(5)
    # if node_to_remove is not None:
    #     node_to_remove.cut_root()

    # minimum = tree.find_min()
    # print(minimum.value)
    # maximum = tree.find_max()
    # print(maximum.value)
    # print(maximum.value)
    # tree.print_tree()
    # tree.print_postorder()
    # print(tree.find_height())