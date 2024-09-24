class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_st = []
        answer = [0] * len(temperatures)

        for curr, val in enumerate(temperatures):
            while temp_st and temp_st[-1][1] < val:
                prev, temp = temp_st.pop()
                answer[prev] = curr - prev
            temp_st.append((curr, val))

        return answer