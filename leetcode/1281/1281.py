class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        add = 0
        result = 0
        product = 1
        for i in str(n):
            i1 = int(i)
            add = add + i1
            product = product*i1
            result = product-add
        return result
sol = Solution()
result = sol.subtractProductAndSum(234)
print(result)