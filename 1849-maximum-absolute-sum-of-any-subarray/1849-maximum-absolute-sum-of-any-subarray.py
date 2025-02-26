class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_so_far = 0
        current_max = 0
        current_min = 0
        for num in nums:
            current_max = max(0, current_max + num)
            max_so_far = max(max_so_far, current_max)
            current_min = min(0, current_min + num)
            max_so_far = max(max_so_far, abs(current_min))
        return max_so_far

        