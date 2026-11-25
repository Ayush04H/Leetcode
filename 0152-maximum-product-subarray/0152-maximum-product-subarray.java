class Solution {
    public int maxProduct(int[] nums) {
        int curr_max = nums[0];
        int curr_min = nums[0];
        int global_max = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int temp_max = curr_max;

            curr_max = Math.max(nums[i], Math.max(nums[i] * temp_max, nums[i] * curr_min));
            curr_min = Math.min(nums[i], Math.min(nums[i] * temp_max, nums[i] * curr_min));

            global_max = Math.max(curr_max, global_max);
        }

        return global_max;
    }
}
