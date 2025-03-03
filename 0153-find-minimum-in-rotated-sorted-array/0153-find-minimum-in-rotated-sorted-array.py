class Solution:
    def findMin(self, arr: List[int]) -> int:
        l = 0 
        h = len(arr) - 1
        while l < h:
            mid = (l+h) // 2

            if arr[mid] > arr[h]:
                l = mid + 1

            else:
                h = mid

        return arr[h]

        