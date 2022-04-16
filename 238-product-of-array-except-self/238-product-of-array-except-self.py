class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
#         O(N) time O(1) space
        length = len(nums)
        answer = [0] * length
        
        answer[0] = 1
        
        for i in range(1, length):
            answer[i] = answer[i-1] * nums[i-1]
            
        
        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer
        
        
#         O(N) space, O(N) time
#         length = len(nums)
        
#         answer = [0]*length
        
#         left = [0]*length
#         right = [0]*length
        
#         left[0] = 1
#         right[length-1] = 1
        
        
#         for i in range(1, length):
#             left[i] = left[i-1]*nums[i-1]
#             right[length-i-1] = right[length-i]*nums[length-i]
            
        
#         for i in range(length):
#             answer[i] = left[i] * right[i]
        
#         return answer
        