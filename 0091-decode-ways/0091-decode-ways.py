class Solution:
    def numDecodings(self, s: str) -> int:
        decode_map = {len(s) : 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                decode_map[i] = 0
            else:
                decode_map[i] = decode_map[i+1]

            if i+1 < len(s):
                digit  = (10 * int(s[i])) + int(s[i+1])

                if 10 <= digit <= 26:
                    decode_map[i] += decode_map[i+2]

        return decode_map[0]
