class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        res = False
        for key , val in count.items():
            if val > 1:
                res = True

        return res
        