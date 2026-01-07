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
        smallerNumbersThanCurrent(self, [8,1,2,2,3])
        smallerNumbersThanCurrent(self, [6,5,4,8])
        smallerNumbersThanCurrent(self, [7,7,7,7])