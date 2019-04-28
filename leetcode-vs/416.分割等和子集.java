/*
 * @lc app=leetcode.cn id=416 lang=java
 *
 * [416] 分割等和子集
 *
 * https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
 *
 * algorithms
 * Medium (37.71%)
 * Total Accepted:    2.2K
 * Total Submissions: 5.9K
 * Testcase Example:  '[1,5,11,5]'
 *
 * 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
 * 
 * 注意:
 * 
 * 
 * 每个数组中的元素不会超过 100
 * 数组的大小不会超过 200
 * 
 * 
 * 示例 1:
 * 
 * 输入: [1, 5, 11, 5]
 * 
 * 输出: true
 * 
 * 解释: 数组可以分割成 [1, 5, 5] 和 [11].
 * 
 * 
 * 
 * 
 * 示例 2:
 * 
 * 输入: [1, 2, 3, 5]
 * 
 * 输出: false
 * 
 * 解释: 数组不能分割成两个元素和相等的子集.
 * 
 * 
 * 
 * 
 */
class Solution {
    public boolean canPartition(int[] nums) {
        /**
         * https://www.cnblogs.com/Christal-R/p/Dynamic_programming.html
         * 空间优化两点:
         * 1. 每一次V(i)(j)改变的值只与V(i-1)(x) {x:1...j}有关，V(i-1)(x)是前一次i循环保存下来的值
         *  可以用一维数组
         * 2. 每一次推导V(i)(j)是通过V(i-1)(j-w(i))来推导的，
         *      所以一维数组中j的扫描顺序应该从大到小(capacity到0)
         *      否则i更新完j-w(i)，i+1可能也更新 j-w(i)
         *      
         */
        int sum = 0;
        for (int a:nums) sum += a;

        if (sum % 2 != 0) return false;

        int v = sum/2;

        int[] dp = new int[v + 1];

        for (int i = 1; i < nums.length; i++) {
            for (int j = v; j >= nums[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }

        return dp[v] == v ? true : false;
    }
}

