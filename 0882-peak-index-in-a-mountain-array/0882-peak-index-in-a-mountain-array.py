class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0 
        hi = len(arr) - 1 
        res = -1
        while l < hi:
            m = (l+hi) // 2
            if arr[m] < arr[m+1]:
                l = m + 1

            else:
                hi = m

        return l

        