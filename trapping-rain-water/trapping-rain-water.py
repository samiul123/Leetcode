class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        ans = 0
        
        while left < right:
            if height[left] < height[right]:
                (leftMax := height[left]) if (height[left] >= leftMax) else (ans := ans + leftMax - height[left])
                left += 1
            else:
                (rightMax := height[right]) if (height[right] >= rightMax) else (ans := ans + rightMax - height[right])
                right -= 1
        return ans
                    