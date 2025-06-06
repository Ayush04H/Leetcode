class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = dict()
        for i,num in enumerate(nums):
            if target-num in dic:
                return[dic[target-num]+1,i+1]
            dic[nums[i]] = i 

        return []
        