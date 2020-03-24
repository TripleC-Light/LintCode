"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and return the root node of this tree.
The size of the given array will be in the range of [1,1000].

Example 1:

Input: {3,2,1,6,0,5}
Output: Return the tree root node representing the following tree:
     6
   /   \
  3     5
   \   / 
    2 0   
     \
      1
Example 2:

Input: {1,2,3,4}
Output: Return the tree root node representing the following tree:
        4
       /
      3
     /
    2
   /
  1    

Definition of TreeNode:"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here

        result = []
        valList = [nums]
        _tmpNums = nums.copy()
        hasNode = True
        while hasNode:
            hasNode = False
            _tmpValList = []
            for vals in valList:
                if len(vals) != 0:
                    #print(max(vals))
                    result.append(max(vals))
                    _tmpNums.remove(max(vals))
                    maxInd = vals.index(max(vals))
                    _tmpValList.append(vals[:maxInd])
                    _tmpValList.append(vals[maxInd+1:])
                    hasNode = True
                else:
                    #print(len(_tmpNums))
                    if len(_tmpNums) != 0:
                        result.append(None)
                        _tmpValList.append([])
                        _tmpValList.append([])
                        
            valList = _tmpValList
            #print(result, valList)

        print(result)
        result = self.genNodeTree(result)
        return result[0]

    def genNodeTree(self, valList):
        result = []
        nodeList = []
        for val in valList:
            nodeList.append(TreeNode(val))
            
        for ind, val in enumerate(nodeList):
            if val.val != None:
                newNode = val
                if (ind*2)+1 < len(nodeList):
                    if nodeList[(ind*2)+1].val != None:
                        newNode.left = nodeList[(ind*2)+1]

                    if nodeList[(ind*2)+2].val != None:
                        newNode.right = nodeList[(ind*2)+2]
                    
                result.append(newNode)
                #print(newNode.val, newNode.left, newNode.right)

        return result
            
if __name__ == '__main__':
    
    A = Solution()
    print(A.constructMaximumBinaryTree([3,2,1,6,0,5]))
    
