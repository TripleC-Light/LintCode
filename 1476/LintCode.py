"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
1.3 <= A.length <= 10000
2.0 <= A[i] <= 10^6

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
"""

class Solution:
    """
    @param A: an array
    @return: any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
    """
    def peakIndexInMountainArray(self, A):
        # Write your code here
        return A.index(max(A))
        

if __name__ == '__main__':

    A = Solution()
    print(A.peakIndexInMountainArray([0,2,1,0]))
    
