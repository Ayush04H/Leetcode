from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = Counter(nums)
        for key,val in res.items():
            if val >len(nums)//2:
                return key
        