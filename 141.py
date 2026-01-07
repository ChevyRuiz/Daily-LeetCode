# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        hashmap = {}
        current = head
        while current.next is not None:
            if current not in hashmap:
                hashmap[current] = 1
            else:
                return True
            current = current.next
        return False
    
    # Optimal with O(1) space complexity - mine was O(n)
"""
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
