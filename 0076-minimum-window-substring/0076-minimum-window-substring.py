class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = ""

        substr_map = {}
        window = {}

        for c in t:
            substr_map[c] = 1 + substr_map.get(c, 0)
        
        have = 0
        need = len(substr_map)
        min_len = float("inf")
        
        left = 0
        for right in range(len(s)):
            if s[right] not in t:
                continue
            
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if window[c] == substr_map[c]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    answer = s[left : right+1]

                c = s[left]
                if c in window:
                    window[c] -= 1
                    if window[c] < substr_map[c]:
                        have -= 1
                
                left += 1

        return answer





