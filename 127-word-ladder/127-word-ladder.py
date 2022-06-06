class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        generics = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                generics[word[:i]+"*"+word[i+1:]].append(word)
                
                
        queue = collections.deque([(beginWord, 1)])
        
        visited = {beginWord}
        
        # print(generics)
        while queue:
            currentWord, level = queue.popleft()
            for i in range(len(currentWord)):
                intermediateWord = currentWord[:i]+"*"+currentWord[i+1:]
                # print(intermediateWord)
                # print(generics[intermediateWord])
                for word in generics[intermediateWord]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, level+1))
                generics[intermediateWord] = []
                
        return 0
                        
        
        