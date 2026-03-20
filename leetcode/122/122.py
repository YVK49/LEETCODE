class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for i in range(n-1):
            if prices[i] < prices[i + 1]:
                profit = profit + (prices[i + 1] - prices[i])
        return profit
sol = Solution()
length = sol.maxProfit([7,1,5,3,6,4])
print(length)