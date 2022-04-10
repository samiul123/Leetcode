

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         O(N^3) TIme (TLE)
#         maxLength = 0
        
#         def is_unique(left, right):
#             frequency = {}
#             for i in range(left, right+1):
#                 if s[i] not in frequency:
#                     frequency[s[i]] = i
#                 else:
#                     return False
#             return True
        
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 if is_unique(i, j):
#                     maxLength = max(maxLength, j - i + 1)
        
#         return maxLength
        
        dic = {}
        
        def increaseCharCount(char):
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1
            
        def decreaseCharCount(char):
            dic[char] -= 1
        
        def getCount(char):
            return dic[char]

        # chars = [0] * 128
        

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            
            # chars[ord(r)] += 1
            
            # increaseCharCount(r)
            dic[r] = 1 if r not in dic else dic[r] + 1

            while dic[r] > 1:
                l = s[left]
                # chars[ord(l)] -= 1
                dic[l] -= 1
                left += 1
            
            res = max(res, right - left + 1)

            right += 1
        return res
        
        