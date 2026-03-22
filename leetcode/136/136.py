class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for num, count in hash_map.items():
            if count == 1:
                return num
        return -1 