# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int: 
        index_to_val_map = {}
        index = 1
        curr = self.head
        while curr:
            index_to_val_map[index] = curr.val
            index += 1
            curr = curr.next

        random_index = random.randint(1, index - 1)

        return index_to_val_map[random_index]


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()