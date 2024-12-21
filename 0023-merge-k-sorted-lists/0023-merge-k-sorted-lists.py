# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def merge(self, left_ll, right_ll):
        curr = ListNode(0)
        merged_ll = curr

        while left_ll and right_ll:
            if left_ll.val <= right_ll.val:
                curr.next = left_ll
                left_ll = left_ll.next
            else:
                curr.next = right_ll
                right_ll = right_ll.next

            curr = curr.next

        if left_ll:
            curr.next = left_ll

        if right_ll:
            curr.next = right_ll
        
        return merged_ll.next

    def divide(self, left, right, lists):
        if right < left:
            return None

        if left == right:
            return lists[left]

        mid = left + (right - left) // 2

        left_ll = self.divide(left, mid, lists)
        right_ll = self.divide(mid + 1, right, lists)

        return self.merge(left_ll, right_ll)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        return self.divide(0, len(lists) - 1, lists)
