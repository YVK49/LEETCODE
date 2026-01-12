class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n= len(nums)
        k=0
        for i in range(0,n):
            if k<2 or nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k=k+1
        return k