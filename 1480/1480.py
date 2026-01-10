class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        result.append(nums[0])
        for i in range(1, n):
            x = result[i-1] + nums[i]
            result.append(x)
        return result
sol = Solution()
result = sol.runningSum([1,2,3,4])