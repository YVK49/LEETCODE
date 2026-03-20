class Solution:
    def reverseVowels(self, s: str) -> str:
            res = list(s)
            n = len(s)
            left = 0
            right = n-1
            vowels = ("aeiouAEIOU")
            while left<right:
                if res[left] not in vowels:
                    left+=1
                elif res[right] not in vowels:
                    right-=1
                else:
                    res[left], res[right]=res[right], res[left]
                    left+=1
                    right-=1
            return "".join(res)