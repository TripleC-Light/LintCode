class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, s, offset):
        # write your code here
        if offset != 0:
            return s[offset+1:]+s[:offset+1]
        else:
            return s
    
if __name__ == '__main__':

    A = Solution()
    print(A.rotateString("abcdefg", 3))
    
