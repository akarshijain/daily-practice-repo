# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2) -> Optional[ListNode]:
        head = ListNode()
        curr = head

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        while l1:
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            curr.next = l2
            curr = curr.next
            l2 = l2.next

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        while len(lists) > 1:
            mergedList = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if i+1 < len(lists) else None
                mergedList.append(self.mergeTwoLists(list1, list2))
            lists = mergedList

        return lists[0]