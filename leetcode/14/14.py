class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        n = len(strs)
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i+=1
        return last[:i]      