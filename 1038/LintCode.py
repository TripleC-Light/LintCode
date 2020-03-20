"""
You're given strings J representing the types of stones that are jewels,
and S representing the stones you have.
Each character in S is a type of stone you have.
You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct,
and all characters in J and S are letters.
Letters are case sensitive,
so "a" is considered a different type of stone from "A".
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
"""
class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        count = 0
        jewelList = list(J)
        for ston in list(S):
            if ston in jewelList:
                count += 1
        
        return count

if __name__ == '__main__':

    A = Solution()
    print(A.numJewelsInStones("aA", "aAAbbbb"))
    
