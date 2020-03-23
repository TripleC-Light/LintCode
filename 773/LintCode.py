"""
Given two strings s and t, write a function to determine if t is an anagram of s.

You may assume the string contains only lowercase alphabets.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution:
    """
    @param s: string s
    @param t: string t
    @return: Given two strings s and t, write a function to determine if t is an anagram of s.
    """
    def isAnagram(self, s, t):
        # write your code here
        _s = list(s)
        _t = list(t)
        _s.sort()
        _t.sort()
        print(_s, _t)
        if _s == _t:
            return True
        else:
            return False

if __name__ == '__main__':

    A = Solution()
    print(A.isAnagram("anagram", "nagaram"))
    
