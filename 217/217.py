class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = {}
        for i in range(len(nums)):
            number = nums[i]
            if number in seen_numbers:
                return True
            seen_numbers[number] = i
        return False
        