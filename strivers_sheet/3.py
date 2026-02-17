class Solution:
    def isPalindrome(self, n):
        n = list(str(abs(n)))
        x = len(n)
        left = 0
        right = x-1
        while left < right:
            if n[left]!=n[right]:
                return False
            left+=1
            right-=1
        return True