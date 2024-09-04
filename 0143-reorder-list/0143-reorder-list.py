# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow  = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        prev = slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp

        left = head
        right = prev

        while right:
            temp_left = left.next
            temp_right = right.next

            left.next = right
            right.next = temp_left
            
            right = temp_right
            left = temp_left
