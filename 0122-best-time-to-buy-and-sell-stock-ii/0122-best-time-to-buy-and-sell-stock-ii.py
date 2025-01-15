class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        prof = 0 
        n = len(arr)
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                prof += arr[i] - arr[i-1]

        return prof
        