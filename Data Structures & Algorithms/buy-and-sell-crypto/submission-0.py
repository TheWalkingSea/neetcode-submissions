class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            price = prices[i]
            if (price > buy):
                maxprofit = max(maxprofit, price - buy)
            else:
                buy = price
        
        return maxprofit
            
        