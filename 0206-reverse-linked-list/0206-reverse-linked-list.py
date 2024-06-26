# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        slow = head
        fast = head.next
        while fast:
            temp = fast.next
            fast.next = slow
            slow = fast
            fast = temp

        head.next = None
        return slow
