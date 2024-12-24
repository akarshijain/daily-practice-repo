class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)

        pattern_map = {}
        for word in wordList:
            for partition in range(len(word)):
                pattern = word[ : partition] + "*" + word[partition + 1 :]
                if pattern not in pattern_map:
                    pattern_map[pattern] = []
                pattern_map[pattern].append(word)

        visited = set([beginWord])
        word_q = deque([beginWord])
        shortest_transformation = 1

        while word_q:
            for _ in range(len(word_q)):
                word = word_q.popleft()

                if word == endWord:
                    return shortest_transformation

                for partition in range(len(word)):
                    pattern = word[ : partition] + "*" + word[partition + 1 :]
                    for w in pattern_map[pattern]:
                        if w not in visited:
                            word_q.append(w)
                            visited.add(w)

            shortest_transformation += 1
            
        return 0