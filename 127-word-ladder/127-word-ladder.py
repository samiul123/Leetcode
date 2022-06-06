class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        
        generics = collections.defaultdict(list)
        for idx, word in enumerate(wordList):
            for i in range(len(word)):
                generics[word[:i]+"*"+word[i+1:]].append(idx)
                
        wordList.append(beginWord)
        queue = collections.deque([(len(wordList)-1, 1)])
        
        visited = {len(wordList)-1}
        
        # print(generics)
        while queue:
            curr_idx, level = queue.popleft()
            currentWord = wordList[curr_idx]
            for i in range(len(currentWord)):
                intermediateWord = currentWord[:i]+"*"+currentWord[i+1:]
                # print(intermediateWord)
                # print(generics[intermediateWord])
                for idx in generics[intermediateWord]:
                    word = wordList[idx]
                    if word == endWord:
                        return level+1
                    if idx not in visited:
                        visited.add(idx)
                        queue.append((idx, level+1))
                generics[intermediateWord] = []
                
        return 0
                        
        
        