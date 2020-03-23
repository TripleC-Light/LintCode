"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
judge if this robot makes a circle, which means it moves back to the original
place finally.

The move sequence is represented by a string. And each move is represent
by a character. The valid robot moves are R (Right), L (Left), U (Up) and
D (down). The output should be true or false representing whether
the robot makes a circle.

Example 1:

Input: "UD"
Output: true
Example 2:

Input: "LL"
Output: false

"""

class Solution:
    """
    @param moves: a sequence of its moves
    @return: if this robot makes a circle
    """
    def judgeCircle(self, moves):
        # Write your code here
        origiPoint = [0, 0]
        _moves = list(moves)
        
        for step in _moves:
            if step == 'U':
                origiPoint[1] += 1
            elif step == 'D':
                origiPoint[1] -= 1
            elif step == 'L':
                origiPoint[0] -= 1
            elif step == 'R':
                origiPoint[0] += 1
        if origiPoint == [0, 0]:
            return True
        else:
            return False

if __name__ == '__main__':

    A = Solution()
    print(A.judgeCircle("UD"))
    
