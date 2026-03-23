class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        target_count = Counter('balloon')
        result = float('inf')
        for char, demand in target_count.items():
            supply = text_count.get(char, 0)
            result = min(result, supply//demand)
        return result