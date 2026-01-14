class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k=0
        for i in range(n):
            if nums[i] != val:
                nums[k]=nums[i]
                k=k+1
        return k
sol = Solution()
length = sol.removeElement([3,2,2,3,4,5,3],3)
print(length)