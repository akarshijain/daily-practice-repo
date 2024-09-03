class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word))
            encoded_str += '#'
            encoded_str += word
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []

        index = 0
        while index < len(s):
            if s[index].isnumeric():
                word_len = ''
                while(s[index] != '#'):
                    word_len += s[index]
                    index += 1
                start = index + 1
                end = index + 1 + int(word_len)
                decoded_str.append(s[start:end])
                index = end

        return decoded_str



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))