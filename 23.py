# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, headLeft, headRigth) -> Optional[ListNode]:
        i = headLeft
        j = headRigth
        newHead = None
        
        if i is None:
            return j
        if j is None:
            return i
        
        if i.val <= j.val:
            newHead = i
            i = i.next
        elif j:
            newHead = j
            j = j.next

        pointer = newHead

        while i is not None and j is not None:
            if i.val <= j.val:
                temp = i.next
                pointer.next = i
                i = temp
            else:
                temp = j.next
                pointer.next = j
                j = temp
            pointer = pointer.next

        while i is not None:
            temp = i.next
            pointer.next = i
            i = temp
            pointer = pointer.next
        while j is not None:
            temp = j.next
            pointer.next = j
            j = temp
            pointer = pointer.next

        return newHead

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newHead = None
        if len(lists) == 1:
            return lists[0]

        for i in range(1, len(lists)):
            newHead = self.mergeTwoLists(lists[i - 1], lists[i])
            lists[i] = newHead
        return newHead
