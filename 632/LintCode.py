"""
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
Example 1:

Input:
{1,-5,3,1,2,-4,-5}
Output: 3
Explanation:
The tree look like this:
     1
   /   \
 -5     3
 / \   /  \
1   2 -4  -5
Example 2

Input:
{10,-5,2,0,3,-4,-5}
Output: 10
Explanation:
The tree look like this:
     10
   /   \
 -5     2
 / \   /  \
0   3 -4  -5 
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val   = val
        self.left  = None
        self.right = None
"""

class Solution:
    """
    @param: root: the root of tree
    @return: the max node
    """
    def maxNode(self, root):
        if root != None:
            valList = []
            allNodeList = []
            valList.append(root.val)
            hasNode = True
            nodeList = [root]
            while hasNode:
                hasNode = False
                nodeNum = len(nodeList) * 2
                tmpNodeList = []
                for node in nodeList:
                    if node != None:
                        if node.left != None:
                            valList.append(node.left.val)
                            hasNode = True
                        if node.right != None:
                            valList.append(node.right.val)
                            hasNode = True
                        tmpNodeList.append(node.left)
                        tmpNodeList.append(node.right)
                        allNodeList.append(node)
                nodeList = tmpNodeList
            return allNodeList[valList.index(max(valList))]

        else:
            return None

if __name__ == '__main__':

    A = Solution()
    print(A.maxNode())
    
