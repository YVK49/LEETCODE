class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        for val in str(num):
            val_int = int(val)
            if num%val_int==0:
                count+=1
        return count

