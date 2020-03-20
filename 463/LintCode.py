"""
Given an integer array, sort it in ascending order. Use selection sort,
bubble sort, insertion sort or any O(n2) algorithm.
Example 1:
	Input:  [3, 2, 1, 4, 5]
	Output: [1, 2, 3, 4, 5]
	
	Explanation: 
	return the sorted array.

Example 2:
	Input:  [1, 1, 2, 1, 1]
	Output: [1, 1, 1, 1, 2]
	
	Explanation: 
	return the sorted array.
"""
class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        flag = True
        for _ in A:
            if flag:
                flag = False
                for i in range(0, len(A)-1):
                    if A[i] > A[i+1]:
                        A[i+1], A[i] = A[i], A[i+1]
                        flag = True
            else:
                break
        return None

if __name__ == '__main__':

    inputArr = [3, 2, 1, 4, 5]
    A = Solution()
    A.sortIntegers(inputArr)
    print(inputArr)
    
