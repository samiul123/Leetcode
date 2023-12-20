class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        str = ''.join(char for char in str if char.isalnum())

        length = len(str)
        left, right = 0, length - 1

        while left < right:
            if str[left] == str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
