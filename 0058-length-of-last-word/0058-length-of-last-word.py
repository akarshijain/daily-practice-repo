class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_word_length = 0
        temp_count = 0
        for char in s:
            if char == " ":
                if temp_count != 0:
                    last_word_length = temp_count
                    temp_count = 0
                continue

            else:
                temp_count += 1

        if temp_count != 0:
            last_word_length = temp_count

        return last_word_length

                