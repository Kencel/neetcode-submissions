# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not any(lists): return None
        INF = 10 ** 9
        out = ListNode(-INF)
        curr = out
        while any(lists):
            mn = ListNode(INF)
            idx = -1
            for i in range(len(lists)):
                if lists[i] and lists[i].val < mn.val:
                    mn.val = lists[i].val
                    idx = i
            lists[idx] = lists[idx].next
            curr.next = mn
            curr = mn
        return out.next
