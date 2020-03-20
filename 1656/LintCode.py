"""
Given n integers and two positive integers L, R,
output how many integers are in the range between [L, R]
L \leq RL≤R
Example 1:

Input: a=[1,2,3,4,5,6],L=3,R=5
Output: 3
Explaination: 
Only a[2],a[3],a[4] are in range of [3,5].
Example 2:

Input: a=[1,5,3,3,3,2],L=1,R=2
Output: 2
Explaination: 
Only a[0],a[5] are in range of [1,2].
"""

class Solution:
    """
    @param a: the array a
    @param L: the integer L
    @param R: the integer R
    @return: Return the number of legal integers
    """
    def getNum(self, a, L, R):
        count = 0
        for item in a:
            if item >= L and item <= R:
                count += 1
                
        return count
        

if __name__ == '__main__':

    A = Solution()
    print(A.getNum([8,5,1,10,5,9], 3, 9))
    
