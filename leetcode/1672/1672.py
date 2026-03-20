class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_amount = 0 
        current_amount = 0
        for i in range(len(accounts)):
            current_amount = sum(accounts[i])
            if current_amount > max_amount:
                max_amount = current_amount
        return max_amount     
sol = Solution()
length = sol.maximumWealth([[1,2,3],[3,2,1]])
print(length)