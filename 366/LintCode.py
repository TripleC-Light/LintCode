"""
Find the Nth number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

The first two numbers are 0 and 1.
The i th number is the sum of i-1 th number and i-2 th number.
The first ten numbers in Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
Example 1:
	Input:  1
	Output: 0
	
	Explanation: 
	return the first number in  Fibonacci sequence .

Example 2:
	Input:  2
	Output: 1
	
	Explanation: 
	return the second number in  Fibonacci sequence .
"""
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        initList = [0, 1]

        for i in range(2, n):
            
            initList.append(initList[i-2] + initList[i-1])

        return initList[n-1]

if __name__ == '__main__':

    A = Solution()
    print(A.fibonacci(10))
    
