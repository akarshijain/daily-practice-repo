class Solution:
    def candy(self, ratings: List[int]) -> int:
        num_candies = [1] * len(ratings)

        for index in range(1, len(ratings)):
            if ratings[index] > ratings[index - 1] \
                and num_candies[index] <= num_candies[index - 1]:
                num_candies[index] = num_candies[index - 1] + 1

        for index in range(len(ratings) - 2, -1, -1):
            if ratings[index] > ratings[index + 1] \
                and num_candies[index] <= num_candies[index + 1]:
                num_candies[index] = num_candies[index + 1] + 1

        return sum(num_candies)
        