class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):  # First element
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):  # Second element
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l = j + 1  # Third element
                r = n - 1  # Fourth element

                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        # Add the quadruplet to the result
                        ans.append([nums[i], nums[j], nums[l], nums[r]])

                        # Skip duplicates for the third element
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1

                        # Skip duplicates for the fourth element
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1

                        # Move both pointers
                        l += 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return ans
                    
        