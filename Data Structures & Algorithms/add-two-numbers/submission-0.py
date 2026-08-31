# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        s = 0
        count = 0
        while l1:
            s += l1.val * 10 ** count
            l1 = l1.next
            count += 1
        count = 0
        while l2:
            s += l2.val * 10 ** count
            l2 = l2.next
            count += 1
        
        if s == 0: return ListNode()
        head = ListNode(s % 10)
        s //= 10
        prev = head
        while s:
            curr = ListNode(s % 10)
            prev.next = curr
            prev = curr
            s //= 10
        return head

