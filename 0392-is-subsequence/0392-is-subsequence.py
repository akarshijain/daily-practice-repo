class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        index_s = 0
        index_t = 0

        while index_t < len(t):
            if index_s >= len(s):
                return True

            if s[index_s] == t[index_t]:
                index_s += 1

            index_t += 1

        if index_s >= len(s):
            return True

        return False