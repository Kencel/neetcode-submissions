# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        if not list1:
            head = list2
            ptr1 = head.next
            ptr2 = None
        elif not list2:
            head = list1
            ptr1 = head.next
            ptr2 = None
        elif list1.val < list2.val:
            head = list1
            ptr1 = head.next
            ptr2 = list2
        else:
            head = list2
            ptr1 = head.next
            ptr2 = list1
        
        curr = head
        while ptr1 or ptr2:
            if not ptr1:
                curr.next = ptr2
                curr = curr.next
                ptr2 = ptr2.next
            elif not ptr2:
                curr.next = ptr1
                curr = curr.next
                ptr1 = ptr1.next
            elif ptr1.val < ptr2.val:
                curr.next = ptr1
                curr = curr.next
                ptr1 = ptr1.next
            else:
                curr.next = ptr2
                curr = curr.next
                ptr2 = ptr2.next
        

        return head