"""
Convert a lowercase character to uppercase.
Example 1:

Input: 'a'
Output: 'A'
Example 2:

Input: 'b'
Output: 'B'
"""
class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        asciiCode = ord(character)
        if asciiCode in range(65, 91):
            return chr(asciiCode+32)
        
        elif asciiCode in range(97, 123):
            return chr(asciiCode-32)     

if __name__ == '__main__':
    
    A = Solution()
    print(A.lowercaseToUppercase("A"))
    
