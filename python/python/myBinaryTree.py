class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node , data):
        if node is None:
            return self.createNode(data)
        if data < node.value:
            node.left = self.insert(node.left, data)
        elif data > node.value:
            node.right = self.insert(node.right, data)
        return node

    def search(self, node, data):
        if (node is None):
            return False
        else:
            if(node.value == data):
                return True
            else:
                if (data < node.value):
                    return self.search(node.left, data)
                else:
                    return self.search(node.right, data)

def main():
    root = None
    tree = Tree()
    root = tree.insert(root, 10)
    print(root)
    tree.insert(root, 20)
    tree.insert(root, 30)
    tree.insert(root, 40)
    tree.insert(root, 70)
    tree.insert(root, 60)
    tree.insert(root, 80)

    print(root)
    print(tree.search(tree, 10))
    # print "Traverse Inorder"
    # tree.traverseInorder(root)

    # print "Traverse Preorder"
    # tree.traversePreorder(root)

    # print "Traverse Postorder"
    # tree.traversePostorder(root)

if __name__ == "__main__":
    main()