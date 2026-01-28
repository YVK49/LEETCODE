class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)
        if idx == -1:
            return word
        chars = list(word)
        left = 0
        right = idx
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left+=1
            right-=1
        return "".join(chars)        