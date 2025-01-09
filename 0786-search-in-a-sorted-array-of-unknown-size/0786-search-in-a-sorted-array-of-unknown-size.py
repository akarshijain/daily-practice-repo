# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        first_out_of_bound_index = 1

        while reader.get(first_out_of_bound_index) != 2**31 - 1 or reader.get(first_out_of_bound_index) <= target:
            first_out_of_bound_index *= 2

        left, right = 0, first_out_of_bound_index - 1
        while left <= right:
            mid = (left + right) // 2
            value = reader.get(mid)

            if value == 2**31 - 1:
                right = mid - 1
                continue

            if value == target:
                return mid

            if value > target:
                right = mid - 1

            else:
                left = mid + 1

        return -1

            
