class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result
sol = Solution()
length = sol.twoSum([2,7,11,15], 9)
print(length)