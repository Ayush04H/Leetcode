from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_freq = sorted(count.items(),key = lambda x:x[1],reverse= True)
        res = [item[0] for item in most_freq[:k]]

        return res

        