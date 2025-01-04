class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_palindromes = set()
        for c in 'abcdefghijklmnopqrstuvwxyz':
            first = s.find(c)
            last = s.rfind(c)
            if first < last:  # Ensure there are characters in between
                for char in s[first + 1:last]:
                    unique_palindromes.add(c + char + c)
        return len(unique_palindromes)

            