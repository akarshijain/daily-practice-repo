class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        line_sweep = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction == 1:
                line_sweep[start] += 1
                line_sweep[end + 1] += -1
            else:
                line_sweep[start] += -1
                line_sweep[end + 1] += 1

        for i in range(1, len(line_sweep)):
            line_sweep[i] += line_sweep[i - 1]

        shifted_str = ""
        for index in range(len(s)):
            relative_ord = ord(s[index]) - ord('a')
            new_ord = relative_ord + line_sweep[index]
            absolute_ord = ord('a') + ((26 + new_ord) % 26)
            shifted_str += chr(absolute_ord)

        return shifted_str
