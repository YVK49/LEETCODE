class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for i in range(0, n):
            current_number = nums[i]
            if current_number in seen:
                return current_number
            seen.add(current_number)