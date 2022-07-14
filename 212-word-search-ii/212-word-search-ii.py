class TrieNode:
    def __init__(self, char):
        self.links = [None] * 26
        self.isEnd = False
        self.char = char
        self.word = ""

    def containsKey(self, char: str) -> bool:
        return self.links[ord(char) - ord('a')] is not None

    def get(self, char: str):
        return self.links[ord(char) - ord('a')]

    def put(self, char: str, node) -> None:
        self.links[ord(char) - ord('a')] = node

    def setEnd(self, isEnd) -> None:
        self.isEnd = isEnd

    def setWord(self, word) -> None:
        self.word = word


class Trie:
    def __init__(self):
        self.root = TrieNode("/")

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if not node.containsKey(letter):
                node.put(letter, TrieNode(letter))
            node = node.get(letter)
        node.setWord(word)
        node.setEnd(True)
    
    # O(len(word))
    def searchPrefix(self, word: str) -> TrieNode or None:
        node = self.root
        for letter in word:
            if not node.containsKey(letter):
                return None
            node = node.get(letter)
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.searchPrefix(prefix)
        return node is not None
    
    def checkIfAnyWordUnderTheNode(self, node):
        if not node:
            return False
        for link in node.links:
            if link and link.isEnd:
                return True
            if self.checkIfAnyWordUnderTheNode(link):
                return True
        return False


def buildTrie(words: List[str]) -> Trie:
    trie = Trie()
    for word in words:
        trie.insert(word)
    return trie


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> set:
        trie = buildTrie(words)
        
        n_rows = len(board)
        n_cols = len(board[0])
        matched_words = set()

        def backtrack(row, col, curr_node):
            letter = board[row][col]
            parentNode = curr_node
            curr_node = curr_node.get(letter)
            if not curr_node:
                return

            if curr_node.isEnd:
                matched_words.add(curr_node.word)
                curr_node.setEnd(False)
                # pruning out the matched word from the trie
                if not trie.checkIfAnyWordUnderTheNode(curr_node):
                    parentNode.put(letter, None)

            board[row][col] = '#'

            for dRow, dCol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row = row + dRow
                new_col = col + dCol
                if new_row < 0 or new_row >= n_rows or new_col < 0 or new_col >= n_cols:
                    continue
                if board[new_row][new_col] == '#':
                    continue
                if not curr_node.containsKey(board[new_row][new_col]):
                    continue
                backtrack(new_row, new_col, curr_node)

            board[row][col] = letter

        for i in range(n_rows):
            for j in range(n_cols):
                backtrack(i, j, trie.root)

        return matched_words

    
    
    
#     def getMap(self, board, words):
#         startingLetterIndexMap = collections.defaultdict(list)
#         # print(len(board))
#         # print(len(board[0]))
#         # print(len(words))
#         for word in words:
#             # print(len(word))
#             for row in range(len(board)):
#                 for col in range(len(board[row])):
#                     if word[0] == board[row][col]:
#                         startingLetterIndexMap[word].append((row, col))
#         return startingLetterIndexMap
    
        
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         n_row = len(board)
#         n_col = len(board[0])
        
#         map = self.getMap(board, words)
#         lettersInBoard = set(map.keys())
#         # print(map)
#         existingWords = []
        
#         for word in words:
#             # print(word)
#             # print(map[word])
#             # print(board)
#             searchIdx = 0
#             lettersInWord = set(word)
#             if n_row * n_col < len(word):
#                 continue
#             # if len(lettersInWord.difference(lettersInBoard.intersection(lettersInWord))):
#             #     continue
#             for startRow, startCol in map[word]:
#                 # print(startRow, startCol)
#                 if self.isExist(board, startRow, startCol, word, searchIdx):
#                     existingWords.append(word)
#                     break
#         return existingWords
    
#     def isExist(self, board, row, col, word, searchIdx):
#         if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or searchIdx >= len(word):
#             return False
        
#         currentChar = board[row][col]
#         if word[searchIdx] != currentChar:
#             return False
    
#         if searchIdx == len(word) - 1:
#             return True
        
#         board[row][col] = "#"
        
#         res = False
#         for dRow, dCol in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
#             res = self.isExist(board, row + dRow, col + dCol, word, searchIdx + 1)
#             if res:
#                 break
                
#         board[row][col] = currentChar
        
#         return res
        
                
        
            
        
        