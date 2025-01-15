class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        res.append(nums[0])
        n = len(nums)
        s = nums[0]
        for i in range(1,n):
            s += nums[i]
            res.append(s)

        return res


        