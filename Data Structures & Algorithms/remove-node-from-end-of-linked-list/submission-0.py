# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next

        if length == 1:
            return None
            
        pos = length - n + 1
        if pos == 1:
            nxt = head.next
            head = nxt
            return head
        
        curr = head
        count = 0
        prev = None
        while curr.next and pos - count != 1:
            prev = curr
            curr = curr.next
            count += 1
        
        nxt = curr.next
        curr.next = None
        prev.next = nxt
        return head