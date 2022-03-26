class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def helper(s, left, right):
            if left >= right:
                return
            
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            helper(s, left+1, right-1)
        
        helper(s, 0, len(s)-1)
        
        