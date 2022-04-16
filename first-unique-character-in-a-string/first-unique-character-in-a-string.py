class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = {}
        
        for c in s:
            charCount[c] = charCount.get(c, 0) + 1
        
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        
        return -1