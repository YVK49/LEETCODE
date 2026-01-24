class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)
        i = 0
        n = len(chars)
        while i < n:
            left = i
            right = min(i+k-1, n-1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left+=1
                right-=1
            i+=2*k
        return "".join(chars)        