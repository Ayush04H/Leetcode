class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = defaultdict(int)
        
        # Step 2: Compute all sums of nums1[i] + nums2[j] and store their frequencies
        for num1 in nums1:
            for num2 in nums2:
                sum_map[num1 + num2] += 1
        
        # Step 3: Compute all sums of nums3[k] + nums4[l] and check if -sum exists in sum_map
        count = 0
        for num3 in nums3:
            for num4 in nums4:
                # Check if the opposite of the current sum exists in the map
                count += sum_map[-(num3 + num4)]
        
        return count
        