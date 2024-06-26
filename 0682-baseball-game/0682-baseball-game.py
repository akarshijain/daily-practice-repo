class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for op in operations:
            if op == "+" and len(scores) >= 2:
                scores.append(scores[-1] + scores[-2])
            elif op == "D" and scores:
                scores.append(2*scores[-1])
            elif op == "C" and scores:
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
