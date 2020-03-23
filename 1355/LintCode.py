"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Example 2:

Input: 3
Output:
[
     [1],
    [1,1],
   [1,2,1]
]
"""

class Solution:
    """
    @param numRows: num of rows
    @return: generate Pascal's triangle
    """
    def generate(self, numRows):
        # write your code here
        initTriangle = [[1]]
        
        for i in range(1, numRows):
            _newRow = [1 for n in range(i+1)]
            
            for j in range(1, i):
                _newRow[j] = initTriangle[i-1][j-1] + initTriangle[i-1][j]
            
            initTriangle.append(_newRow)

        return initTriangle
        
if __name__ == '__main__':

    A = Solution()
    print(A.generate(5))
    
