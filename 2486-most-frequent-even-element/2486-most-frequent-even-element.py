class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [num for num in nums if num % 2 == 0]
    
        # If no even numbers, return -1
        if not even_nums:
            return -1

        # Count the frequency of even numbers
        counts = Counter(even_nums)
        
        # Find the most frequent even number
        max_count = 0
        result = float('inf')  # Initialize to a large value

        for num, count in counts.items():
            # Check for the highest frequency, and in case of tie, the smallest number
            if count > max_count or (count == max_count and num < result):
                max_count = count
                result = num

        return result
        