class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        if not words:
            return ""
        def get_vowel_count(word):
            vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
            count = 0
            for char in word:
                if char in vowels:
                    count += 1
            return count
        target_count = get_vowel_count(words[0])
        for i in range(1, len(words)):
            if get_vowel_count(words[i]) == target_count:
                words[i] = words[i][::-1]
        return " ".join(words)
