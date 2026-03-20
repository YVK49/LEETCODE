class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0
        n = len(batteryPercentages)
        for i in range(n):
            if batteryPercentages[i] > 0:
                tested_devices = tested_devices+1
                for j in range(i+1, n):
                    batteryPercentages[j] = batteryPercentages[j] - 1
        return tested_devices
sol = Solution()
length = sol.countTestedDevices([5,0,3,1,2])
print(length)        
