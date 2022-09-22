class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left, right = 0, 0
        
        while right < len(s):
            if s[right] == " " or right == len(s) - 1:
                wordEnd = right - 1 if s[right] == " " else right
                while left < wordEnd:
                    s[left], s[wordEnd] = s[wordEnd], s[left]
                    left += 1
                    wordEnd -= 1
                left = right + 1
            right += 1
        
        return "".join(s)