class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def inorder_traversal(self, root, arr):
        if not root:
            return
        self.inorder_traversal(root.left, arr)
        arr.append(root.data)
        self.inorder_traversal(root.right, arr)
    def merge_arrays(self, arr1, arr2):
        i=j=0
        merged=[]
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                merged.append(arr1[i])
                i+=1
            else:
                merged.append(arr2[j])
                j+=1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged
    def merge_bsts(self, root1, root2):
        arr1, arr2=[], []
        self.inorder_traversal(root1, arr1)
        self.inorder_traversal(root2, arr2)
        merged=self.merge_arrays(arr1, arr2)
        return merged
if __name__=="__main__":
    sol=Solution()
    root1=Node(3)
    root1.left=Node(1)
    root1.right=Node(5)
    root2=Node(4)
    root2.left=Node(2)
    root2.right=Node(6)
    res=sol.merge_bsts(root1, root2)
    print(*res)
