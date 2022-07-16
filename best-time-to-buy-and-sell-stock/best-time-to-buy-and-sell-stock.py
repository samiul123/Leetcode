class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left, right = 0, 1
        maxprofit = 0
        while right < len(prices):
            currprofit = prices[right] - prices[left]
            
            if currprofit <= 0:
                left = right
                right += 1
            else:
                maxprofit = max(maxprofit, currprofit)
                right += 1
        
        return maxprofit