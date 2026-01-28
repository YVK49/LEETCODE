 class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        j = 0
        count = 0
        n1 = len(arr1)
        n2 = len(arr2)
        for i in range(n1):
            while j < n2 and arr1[i] - arr2[j] > d:
                j+=1
            if j < n2 and abs(arr1[i] - arr2[j]) <= d:
                continue
            else:
                count+=1
        return count