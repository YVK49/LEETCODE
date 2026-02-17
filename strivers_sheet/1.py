class Solution:
    def countDigit(self, n):
        count = 0
        n = len(str(abs(n)))
        for i in range(n):
            count += 1
        return count