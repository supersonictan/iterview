/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子序和
 *
 * https://leetcode-cn.com/problems/maximum-subarray/description/
 *
 * algorithms
 * Easy (42.77%)
 * Total Accepted:    39.4K
 * Total Submissions: 92K
 * Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
 *
 * 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
 * 
 * 示例:
 * 
 * 输入: [-2,1,-3,4,-1,2,1,-5,4],
 * 输出: 6
 * 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 * 
 * 
 * 进阶:
 * 
 * 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
 * 
 */
class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length == 0) return 0;

        /*
        * sum[i] 表示以 i 元素结尾的最大和
        * max[i] 表示到 i 为止的最大和
        * TODO:可以优化空间复杂度
        */
        int[] sum = new int[nums.length];
        int[] max = new int[nums.length];
        sum[0] = nums[0];
        max[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            sum[i] = Math.max(nums[i], nums[i] + sum[i-1]);
            max[i] = Math.max(sum[i], max[i-1]);
        }
        return max[nums.length-1];
    }
}

