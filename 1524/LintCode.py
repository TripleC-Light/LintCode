"""
Given the root of a binary search tree (BST) and a value.

Return the node whose value equals the given value. If such node doesn't exist, return null.

Example 1:

Input: value = 2
        4
       / \
      2   7
     / \
    1   3
Output: node 2
Example 2:

Input: value = 5
        4
       / \
      2   7
     / \
    1   3
Output: null
"""

"""Definition of TreeNode:"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        
        hasNode = True
        nodeList = [root]
        while hasNode:
            hasNode = False
            result = None
            _tmpNodeList = []
            
            for node in nodeList:
                if node.val == val:
                    return node.val

                if node.left != None:
                    hasNode = True
                    _tmpNodeList.append(node.left)
                if node.right != None:
                    hasNode = True
                    _tmpNodeList.append(node.right)

            nodeList = _tmpNodeList
            
    
class genNodeTree:
    def __init__(self, treeList):
        _bTree = []
        for ind, val in enumerate(treeList):
            _node = TreeNode(val)
            _bTree.append(_node)
        result = []
        for ind, val in enumerate(_bTree):
            if (ind*2)+1 < len(_bTree):
                _bTree[ind].left = _bTree[(ind*2) + 1]
                _bTree[ind].right = _bTree[(ind*2) + 2]
            if _bTree[ind].val != None:
                result.append(_bTree[ind])
        self.bTree = result
        self.root = result[0]

    def printTree(self):
        hasNode = True
        nodeList = [self.root]
        tmpNodeList = []
        while hasNode:
            hasNode = False
            tmpNodeList = []
            for node in nodeList:
                if node.val == None:
                    print('# ', end='')
                else:
                    print(node.val, ' ', end='')
                if node.left != None:
                    tmpNodeList.append(node.left)
                    hasNode = True
                if node.right != None:
                    tmpNodeList.append(node.right)
                    hasNode = True
            print('')
            print('')
            nodeList = tmpNodeList
            
if __name__ == '__main__':
    
    bTree = genNodeTree([4, 2, 7, 1, 3, None, None])
    bTree.printTree()
    
    A = Solution()
    print(A.searchBST(bTree.root, 2))
    
