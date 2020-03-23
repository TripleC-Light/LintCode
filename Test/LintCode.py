class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        result = []
        for i in range(int(pow(10, n)/10), pow(10, n)):
            intList = list(str(i))
            sumN = 0
            for j in intList:
                sumN += pow(int(j), n)

            #print(intList, sumN)
            if i == sumN:
                result.append(i)
        
        return result
    
if __name__ == '__main__':

    A = Solution()
    print(A.getNarcissisticNumbers(3))
    
