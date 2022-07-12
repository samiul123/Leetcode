class TrieNode:
    def __init__(self):
        self.links = [None]*26
        self.isEnd = False

    def containsKey(self, char: str) -> bool:
        return self.links[ord(char) - ord('a')] is not None

    def get(self, char: str):
        return self.links[ord(char) - ord('a')]

    def put(self, char: str, node) -> None:
        self.links[ord(char) - ord('a')] = node

    def setEnd(self) -> None:
        self.isEnd = True


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for letter in word:
            if not node.containsKey(letter):
                node.put(letter, TrieNode())
            node = node.get(letter)
        node.setEnd()

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

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)