class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = list(str(abs(x)))
        n = len(x)
        left = 0
        right = n-1
        while left < right:
            x[left], x[right] = x[right], x[left]
            left+=1
            right-=1
        reversed_num = sign*int("".join(x))
        if reversed_num < -2**31 or reversed_num > 2**31 - 1:
            return 0
        return reversed_num
        