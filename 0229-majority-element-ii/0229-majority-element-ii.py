from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = Counter(nums)
        result = []
        for key,val in res.items():
            if val > n//3:
                result.append(key)

        return result


        
        