class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0 # Even pointer (0, 2, 4...)
        j = 1 # Odd pointer (1, 3, 5...)
        n = len(nums)
        
        while i < n and j < n:
            # If even index already has an even number, move to next even index
            if nums[i] % 2 == 0:
                i += 2
            # If odd index already has an odd number, move to next odd index
            elif nums[j] % 2 != 0:
                j += 2
            # Both are in the wrong spots! Swap them
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
                
        return nums