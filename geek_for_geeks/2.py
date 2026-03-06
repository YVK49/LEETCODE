class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n = len(arr)
        start = 0
        current_sum = 0
        min_len = n+1
        for end in range(n):
            current_sum += arr[end]
            while current_sum > x:
                min_len = min(min_len, end-start+1)
                current_sum-=arr[start]
                start+=1
        if min_len > n:
            return 0
        return min_len