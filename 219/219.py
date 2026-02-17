class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen_numbers = {}
        for i in range(len(nums)):
            number = nums[i]
            if number in seen_numbers:
                if i - seen_numbers[number] <= k:
                    return True
            seen_numbers[number] = i
        return False