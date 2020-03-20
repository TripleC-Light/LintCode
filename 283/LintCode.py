"""
Convert a lowercase character to uppercase.
Example 1:
	Input:  num1 = 1, num2 = 9, num3 = 0
	Output: 9
	
	Explanation: 
	return the Max of them.

Example 2:
	Input:  num1 = 1, num2 = 2, num3 = 3
	Output: 3
	
	Explanation: 
	return the Max of them.
"""
class Solution:
    """
    @param num1: An integer
    @param num2: An integer
    @param num3: An integer
    @return: an interger
    """
    def maxOfThreeNumbers(self, num1, num2, num3):
        # write your code here
        numList = [num1, num2, num3]
        return max(numList)       

if __name__ == '__main__':
    
    A = Solution()
    print(A.maxOfThreeNumbers(5,6,7))
    
