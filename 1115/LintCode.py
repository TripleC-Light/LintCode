"""
Given a non-empty binary tree,
return the average value of the nodes on each level in the form of an array.
Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5,
and on level 2 is 11. Hence return [3, 14.5, 11].
"""

#Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the binary tree of the  root
    @return: return a list of double
    """
    def averageOfLevels(self, root):
        hasNode = True
        nodeList = [root]
        tmpNodeList = []
        result = []
        while hasNode:
            hasNode = False
            valSum = 0
            valCount = 0
            for node in nodeList:
                if node.val != None:
                    valSum += node.val
                    valCount += 1
                    if node.left != None:
                        tmpNodeList.append(node.left)
                        hasNode = True
                    if node.right != None:
                        tmpNodeList.append(node.right)
                        hasNode = True
                    
            result.append(valSum/valCount)
            nodeList = tmpNodeList
            tmpNodeList = []
        return result

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

    bTree = genNodeTree([3, 9, 20, None, None, 15, 7])
    bTree.printTree()

    A = Solution()
    print(A.averageOfLevels(bTree.root))
    
