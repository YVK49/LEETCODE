class Solution:
    def captureForts(self, forts: List[int]) -> int:
        left = 0
        max_captured = 0
        for right in range(len(forts)):
            if forts[right] !=0:
                if forts[left] == -forts[right] and forts[left]!=0:
                    captured = right-left-1
                    if captured > max_captured:
                        max_captured = captured
                left = right
        return max_captured