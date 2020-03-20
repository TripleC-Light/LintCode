"""
Write a function that takes an unsigned integer and
returns the number of ’1' bits the corresponding binary number
has (also known as the Hamming weight).
Example 1

Input：n = 11
Output：3
Explanation：11(10) = 1011(2), so return 3
Example 2

Input：n = 7
Output：3
Explanation：7(10) = 111(2), so return 3
"""
class Solution:
    """
    @param n: an unsigned integer
    @return: the number of ’1' bits
    """
    def hammingWeight(self, n):
        binNum = bin(n)
        return binNum .count('1')

if __name__ == '__main__':

    A = Solution()
    print(A.hammingWeight(11))
    
