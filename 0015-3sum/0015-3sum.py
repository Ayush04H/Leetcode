class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n-2):
            l = i+1
            r = n -1 
            while l<r:
                s = nums[i] + nums[r] + nums[l]
                if s == 0:
                    ans.add((nums[i],nums[r],nums[l]))
                    l+=1
                    r-=1

                elif s<0:
                    l+=1

                else:
                    r-=1

        return [list(triplet) for triplet in ans]

        