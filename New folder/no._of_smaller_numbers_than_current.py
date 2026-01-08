class Solution():
    def smallerNumbersThanCurrent(self, nums):
        result = []
        for i in nums:
            count = 0
            for j in nums:
                if j < i:
                    count += 1
            result.append(count)
        return result
sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))  # Output: [4,0,1,1,3]