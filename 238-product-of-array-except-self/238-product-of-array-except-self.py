class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        answer = [0]*length
        
        left = [0]*length
        right = [0]*length
        
        left[0] = 1
        right[length-1] = 1
        
        
        for i in range(1, length):
            left[i] = left[i-1]*nums[i-1]
            right[length-i-1] = right[length-i]*nums[length-i]
        
        # for i in range(length-2, -1, -1):
        #     right[i] = right[i+1]*nums[i+1]
        
        
        for i in range(length):
            answer[i] = left[i] * right[i]
        
        return answer
        