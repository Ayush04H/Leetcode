class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        counts = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] * nums[j] not in counts:
                    counts[nums[i] * nums[j]] = 1
                else:
                    counts[nums[i] * nums[j]] += 1
        res = 0
        for freq in counts.values():
            pairs = comb(freq, 2)
            res += 8 * pairs
        return res