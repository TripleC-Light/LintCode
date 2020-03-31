
class TreeNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None


class Solution:
    def __init__(self):
        self.bTree = []

    def genNodeTree(self, nodeList):
        for node in nodeList:
            self.bTree.append(TreeNode(node))

        _treeLen = len(self.bTree)
        for ind, node in enumerate(self.bTree):
            if (ind*2)+1 < _treeLen:
                node.left = self.bTree[(ind*2)+1]
            if (ind*2)+2 < _treeLen:
                node.right = self.bTree[(ind*2)+2]

        self.preOrder(self.bTree[0])
        print('--------------')
        self.inOrder(self.bTree[0])
        print('--------------')
        self.postOrder(self.bTree[0])
        print('--------------')
        
    def preOrder(self, root):
        if root:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val)
            
if __name__ == '__main__':
    
    A = Solution()
    nodeList = [3, 2, 1, 6, 0, 5, 0]
    A.genNodeTree(nodeList)
