class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()

        for i in range(n - 3):  # First element
            for j in range(i + 1, n - 2):  # Second element
                l = j + 1  # Third element
                r = n - 1  # Fourth element

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if s == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    
                    elif s < target:
                        l += 1
                    
                    else:
                        r -= 1
        
        return [list(quadruplet) for quadruplet in ans]
                    
        