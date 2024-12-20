# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        head = result

        carry = 0
        while l1 and l2:
            num_sum = l1.val + l2.val + carry
            temp = ListNode(num_sum % 10)
            carry = num_sum // 10

            result.next = temp

            l1 = l1.next
            l2 = l2.next
            result = result.next

        while l1:
            num_sum = l1.val + carry
            temp = ListNode(num_sum % 10)
            carry = num_sum // 10

            result.next = temp

            l1 = l1.next
            result = result.next

        while l2:
            num_sum = l2.val + carry
            temp = ListNode(num_sum % 10)
            carry = num_sum // 10

            result.next = temp

            l2 = l2.next
            result = result.next

        if carry:
            temp = ListNode(carry)
            result.next = temp

        return head.next



        