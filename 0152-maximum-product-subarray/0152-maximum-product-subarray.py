class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)

        minProduct, maxProduct = 1, 1

        for num in nums:
            temp = minProduct
            minProduct = min(num * minProduct, num * maxProduct, num)
            maxProduct = max(num * temp, num * maxProduct, num)

            result = max(result, maxProduct)

        
        return result
        