class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t<0: return False
        seen={}        
        for i,n in enumerate(nums):
            bkt=n//(t+1)
            if bkt in seen and i-seen[bkt][0]<=k: return True
            if bkt-1 in seen and i-seen[bkt-1][0]<=k and abs(n-seen[bkt-1][1])<=t: return True
            if bkt+1 in seen and i-seen[bkt+1][0]<=k and abs(n-seen[bkt+1][1])<=t: return True
            seen[bkt]=(i,n)
        return False