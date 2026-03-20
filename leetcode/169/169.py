class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max_count = {}
        n = len(nums)
        for num in nums:
            max_count[num] = max_count.get(num, 0) +1
            if max_count[num]  > n/2:
                return num
        return -1
        