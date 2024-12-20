class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_left = height[left]
        max_right = height[right]

        total_trapped_water = 0
        while left < right:
            if max_left <= max_right:
                left += 1
                trapped_water = max_left - height[left]
                if trapped_water > 0:
                    total_trapped_water += trapped_water

                max_left = max(max_left, height[left])

            else:
                right -= 1
                trapped_water = max_right - height[right]
                if trapped_water > 0:
                    total_trapped_water += trapped_water

                max_right = max(max_right, height[right])

        return total_trapped_water