class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        k=0
        for i in range(n):
            if nums[i]%2==0:
                nums[k], nums[i]=nums[i], nums[k]
                k=k+1
        return nums
sol = Solution()
length = sol.sortArrayByParity([3,1,2,4])
print(length)