class Solution:
    def firstUniqChar(self, s: str) -> int:
        charCount = collections.defaultdict(int)
        
        for c in s:
            charCount[c] += 1
        
        for i in range(len(s)):
            if charCount[s[i]] == 1:
                return i
        
        return -1