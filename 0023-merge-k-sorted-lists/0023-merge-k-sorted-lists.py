# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_two_lists(self, list1, list2):
        if not list1:
            return list2
        
        if not list2:
            return list1

        head = ListNode()
        curr = head
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        
        if list2:
            curr.next = list2

        return head.next

        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        list_q = deque(lists)

        while len(list_q) > 1:
            list1 = list_q.popleft()
            list2 = list_q.popleft() if list_q else None
            # merged_list = self.merge_two_lists(list1, list2)
            list_q.append(self.merge_two_lists(list1, list2))

        return list_q[0]