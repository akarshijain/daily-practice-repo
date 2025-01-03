"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new_map = {}
        curr = head
        while curr:
            old_to_new_map[curr] = Node(curr.val)
            curr = curr.next

        deep_copy_head = Node(0)
        curr_copy = deep_copy_head
        curr = head
        while curr:
            curr_copy.next = old_to_new_map[curr]
            curr_copy.next.next = None if not curr.next else old_to_new_map[curr.next]
            curr_copy.next.random = None if not curr.random else old_to_new_map[curr.random]

            curr_copy = curr_copy.next
            curr = curr.next

        return deep_copy_head.next


