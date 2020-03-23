"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"

"""

class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        # Write your code here
        strList = []
        for char in list(str):
            lowerChar = char
            if ord(char) >= 65 and ord(char) <= 90:
                lowerChar = chr(ord(char)+32)

            strList.append(lowerChar)

        return "".join(strList)
            
if __name__ == '__main__':
    
    A = Solution()
    print(A.toLowerCase("Hello"))
    
