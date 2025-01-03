class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        res = arr[0]
        maxi = arr[0]
        n = len(arr)
        for i in range(1,n):
            
            maxi = max(maxi + arr[i] , arr[i])

            res = max(maxi,res)

        return res
        