# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        node_map = {}

        while curr:
            if curr in node_map:
                return True
            node_map[curr] = None
            curr = curr.next

        return False