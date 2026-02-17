class Solution:
    def reverseNumber(self, n):
        n = list(str(abs(n)))
        x = len(n)
        left = 0
        right = x-1
        while left < right:
            n[left], n[right] = n[right], n[left]
            left+=1
            right-=1
        return int("".join(n))