class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0: return False
        
        # Special case for valueDiff = 0
        if valueDiff == 0:
            seen = {}
            for i, n in enumerate(nums):
                if n in seen and i - seen[n] <= indexDiff:
                    return True
                seen[n] = i
            return False
            
        # Standard case using buckets
        bucket = {}
        w = valueDiff
        
        for i, n in enumerate(nums):
            buck = n // w
            
            if buck in bucket:
                return True
                
            if buck - 1 in bucket and abs(n - bucket[buck - 1]) <= valueDiff:
                return True
            if buck + 1 in bucket and abs(n - bucket[buck + 1]) <= valueDiff:
                return True
                
            bucket[buck] = n
            
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // w]
        
        return False