class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            char_list = list(words[i])
            left = 0
            right = len(char_list) - 1
            while left < right:
                char_list[left], char_list[right] = char_list[right], char_list[left]
                left += 1
                right -= 1
            words[i] = "".join(char_list)
        return " ".join(words)