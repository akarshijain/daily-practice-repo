class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = [], []

        if len(nums1) <= len(nums2):
            arr1, arr2 = nums1, nums2
        else:
            arr1, arr2 = nums2, nums1

        total_len = len(nums1) + len(nums2)

        isEven = False
        if total_len % 2 == 0:
            isEven = True

        half = total_len // 2

        left = 0
        right = len(arr1) - 1

        while True:
            mid = (left + right) // 2
            diff = half - mid - 2

            arr1_right = arr1[mid + 1] if (mid + 1) < len(arr1) else float("inf")
            arr2_right = arr2[diff + 1] if (diff + 1) < len(arr2) else float("inf")

            arr1_left = arr1[mid] if mid >= 0 else float("-inf")
            arr2_left = arr2[diff] if diff >= 0 else float("-inf")

            if arr2_left <= arr1_right \
                and arr1_left <= arr2_right:
                if isEven:
                    return (min(arr1_right, arr2_right) \
                            + max(arr1_left, arr2_left)) / 2
                else:
                    return min(arr1_right, arr2_right)

            elif arr1_left > arr2_right:
                right = mid - 1

            else:
                left = mid + 1

                