class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word
            # include hash for word lengths that are grater than 1 digit

        return encoded_str
        
    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i : j])
            decoded_str.append(s[j + 1 : j + 1 + word_len])

            i = j + 1 + word_len

        return decoded_str


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))