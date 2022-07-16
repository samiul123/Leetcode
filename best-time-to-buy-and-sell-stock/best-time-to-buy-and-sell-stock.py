class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        maxprofit = 0
        for right in range(1, len(prices)):
            currprofit = prices[right] - prices[left]
            
            if currprofit < 0:
                left = right
            else:
                maxprofit = max(maxprofit, currprofit)
        
        return maxprofit