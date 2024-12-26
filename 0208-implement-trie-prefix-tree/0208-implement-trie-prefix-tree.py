class TrieNode:
    def __init__(self):
        self.alphabets = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.alphabets:
                curr.alphabets[char] = TrieNode()

            curr = curr.alphabets[char]

        curr.end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if char not in curr.alphabets:
                return False
            curr = curr.alphabets[char]

        if not curr.end_of_word:
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if char not in curr.alphabets:
                return False
            curr = curr.alphabets[char]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)