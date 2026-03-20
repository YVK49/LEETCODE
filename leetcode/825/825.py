class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        ages.sort()
        n = len(ages)
        total_requests = 0
        left = 0
        right = 0
        for i in range(n):
            while right < n and ages[right] <= ages[i]:
                right += 1
            while left < n and ages[left] <= 0.5 * ages[i] + 7:
                left += 1
            if right > left:
                total_requests += (right - left - 1)
        return total_requests