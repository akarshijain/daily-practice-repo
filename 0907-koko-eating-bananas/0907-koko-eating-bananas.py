class Solution:
    def canEat(self, eating_rate: int, hours_given: int, piles: List[int]):
        hours_taken = 0

        for num_bananas in piles:
            hours_taken += math.ceil(float(num_bananas) / eating_rate)

        print(eating_rate, hours_taken)
        return hours_taken <= hours_given

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        k = right

        while left <= right:
            mid = (left + right) // 2

            if self.canEat(mid, h, piles):
                k = mid
                right = mid - 1

            else:
                left = mid + 1

        return k


        