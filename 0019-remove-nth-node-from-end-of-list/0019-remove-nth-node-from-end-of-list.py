# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        length = 0

        while temp:
            length += 1
            temp = temp.next

        if length == n:
            if head.next:
                head = head.next
            else:
                head = None
            return head

        curr = head
        index = 1
        while curr and index < length - n:
            curr = curr.next
            index += 1
        del_node = curr.next
        curr.next = del_node.next
        del_node.next = None

        return head
        

        