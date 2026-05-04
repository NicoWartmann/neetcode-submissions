# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = -1
        val_list = [head]
        while head:
            val_list.append(head)
            if head.next in val_list:
                index = val_list.index(head.next)
                head = None
            else:
                head = head.next
        return bool(index >= 0)