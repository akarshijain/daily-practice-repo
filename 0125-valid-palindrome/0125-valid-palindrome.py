class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s.lower() if char.isalnum())
        i = 0
        j = len(s) - 1
        while j >= i:
            if s[j] != s[i]:
                return False
            j -= 1
            i += 1

        return True