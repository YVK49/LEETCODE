class Solution:
    def twoRepeated(self, arr):
        res = []
        seen = set()
        for i in arr:
            if i in seen:
                res.append(i)
            else:
                seen.add(i)
        return res