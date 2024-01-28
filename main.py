class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


# Завдання 1
def find_max_value(node):
    current = node
    # просуваємось прворуч до останнього вузла
    while current.right is not None:
        current = current.right
    return current.val


# Завдання 2
def find_min_value(node):
    current = node
    # просуваємось ліворуч до останнього вузла
    while current.left is not None:
        current = current.left
    return current.val


# Завдання 3
def sum_tree(node):
    if node is None:
        return 0
    return node.val + sum_tree(node.left) + sum_tree(node.right)


def main():
    # створюємо ДДП
    root = Node(15)
    root = insert(root, 10)
    root = insert(root, 25)
    root = insert(root, 17)
    root = insert(root, 20)

    print("Найбільше значення у дереві:", find_max_value(root))
    print("Найменше значення у дереві:", find_min_value(root))
    print("Сума всіх значень у дереві:", sum_tree(root))


if __name__ == "__main__":
    main()
