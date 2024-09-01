class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        print(nums)
        for i, val in enumerate(nums):
            print(val)
            if val > 0:
                break
            
            if i > 0 and val == nums[i - 1]:
                continue

            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return answer