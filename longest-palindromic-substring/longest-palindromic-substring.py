class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ""
        longestPalindromeLength = 0
        
        for i in range(len(s)):
            # odd length
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                if currLength > longestPalindromeLength:
                    longestPalindrome = s[left: right + 1]
                    longestPalindromeLength = currLength
                left -= 1
                right += 1
                
            # even length
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                currLength = right - left + 1
                if currLength > longestPalindromeLength:
                    longestPalindrome = s[left: right + 1]
                    longestPalindromeLength = currLength
                left -= 1
                right += 1
                
        return longestPalindrome