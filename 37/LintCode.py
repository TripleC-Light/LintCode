"""
Reverse a 3-digit integer.
Example 1:

Input: number = 123
Output: 321
Example 2:

Input: number = 900
Output: 9
"""
class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        numberStr = list(str(number))
        tmp = numberStr[2]
        numberStr[2] = numberStr[0]
        numberStr[0] = tmp
        return int('_'.join(numberStr))     

if __name__ == '__main__':
    
    A = Solution()
    print(A.reverseInteger(123))
    
