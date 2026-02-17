class Solution:
    def divisors(self, n):
        res = []
        for i in range(n):
            if n%i == 0:
                res.append(i)
        return res