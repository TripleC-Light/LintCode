"""
Count how many nodes in a linked list.
Example 1:
	Input:  1->3->5->null
	Output: 3
	
	Explanation: 
	return the length of the list.

Example 2:
	Input:  null
	Output: 0
	
	Explanation: 
	return the length of list.
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        i = 0
        # nextNode = head
        while head:
            head = head.next
            i += 1
        return i    

if __name__ == '__main__':
    
    A = Solution()
    print(A.countNodes())
    
