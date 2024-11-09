class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        temperature_stack = []
        
        for i, temperature in enumerate(temperatures):
            if not temperature_stack or temperature <= temperature_stack[-1][1]:
                temperature_stack.append((i, temperature))

            while temperature_stack and temperature > temperature_stack[-1][1]:
                index, _ = temperature_stack.pop()
                answer[index] = i - index

            temperature_stack.append((i, temperature))

        return answer

            

        