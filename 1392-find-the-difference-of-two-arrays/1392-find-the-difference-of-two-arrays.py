class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set()
        for num in nums1:
            nums1_set.add(num)

        nums2_set = set()
        for num in nums2:
            nums2_set.add(num)

        unique_nums1 = []
        for num in nums1_set:
            if num not in nums2_set:
                unique_nums1.append(num)

        unique_nums2 = []
        for num in nums2_set:
            if num not in nums1_set:
                unique_nums2.append(num)

        answer = [unique_nums1, unique_nums2]

        return answer