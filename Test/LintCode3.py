"""
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

You may assume that each input would have exactly one solution

Example1:
numbers=[2, 7, 11, 15], target=9
return [0, 1]
Example2:
numbers=[15, 2, 7, 11], target=9
return [1, 2]
"""

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        for ind1, val1 in enumerate(numbers):
            for ind2, val2 in enumerate(numbers):
                if ind1 != ind2:
                    if (val1 + val2) == target:
                        return [ind1, ind2]
        

if __name__ == '__main__':

    A = Solution()
    print(A.twoSum([2,7,11,15], 9))
    
