class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def delete_node(self, root, key):
        if root is None:
            return None
        if key<root.data:
            root.left=self.delete_node(root.left, key)
        elif key>root.data:
            root.right=self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp=root.right
            while temp.left is not None:
                temp=temp.left
            root.data=temp.data
            root.right=self.delete_node(root.right, temp.data)
        return root
if __name__=="__main__":
    sol=Solution()
    root=Node(5)
    root.left=Node(3)
    root.right=Node(6)
    root.left.left=Node(2)
    root.left.right=Node(4)
    root.right.right=Node(7)
    key=3
    root=sol.delete_node(root, key)
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    print("BST after deleting node:")
    inorder(root)