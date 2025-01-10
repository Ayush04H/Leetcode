class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1
        counts = Counter(even_nums)
        
        max_count = 0
        result = float('inf')  

        for num, count in counts.items():
        
            if count > max_count or (count == max_count and num < result):
                max_count = count
                result = num

        return result
        