class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0] * len(boxes)
        balls = int(boxes[0])
        for index in range(1, len(boxes)):
            prefix[index] = balls + prefix[index - 1]
            balls += int(boxes[index])

        postfix = [0] * len(boxes)
        balls = int(boxes[-1])
        for index in range(len(boxes) - 2, -1, -1):
            postfix[index] = balls + postfix[index + 1]
            balls += int(boxes[index])

        answer = []
        for index in range(len(boxes)):
            answer.append(prefix[index] + postfix[index])
            
        return answer
