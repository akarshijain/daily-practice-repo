class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_index = len(nums1) - len(nums2) - 1
        nums2_index = len(nums2) - 1

        for i in range(len(nums1) - 1, -1, -1):
            if nums1_index >= 0 and nums2_index >= 0:
                if nums1[nums1_index] >= nums2[nums2_index]:
                    nums1[i] = nums1[nums1_index]
                    nums1_index -= 1
                else:
                    nums1[i] = nums2[nums2_index]
                    nums2_index -= 1

            elif nums1_index >= 0:
                nums1[i] = nums1[nums1_index]
                nums1_index -= 1

            elif nums2_index >= 0:
                nums1[i] = nums2[nums2_index]
                nums2_index -= 1