/*
 * @lc app=leetcode.cn id=215 lang=java
 *
 * [215] 数组中的第K个最大元素
 *
 * https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
 *
 * algorithms
 * Medium (56.44%)
 * Total Accepted:    16.6K
 * Total Submissions: 29.4K
 * Testcase Example:  '[3,2,1,5,6,4]\n2'
 *
 * 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
 * 
 * 示例 1:
 * 
 * 输入: [3,2,1,5,6,4] 和 k = 2
 * 输出: 5
 * 
 * 
 * 示例 2:
 * 
 * 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
 * 输出: 4
 * 
 * 说明: 
 * 
 * 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
 * 
 */
class Solution {
    public int findKthLargest(int[] nums, int k) {
        return kThPartition(nums, k, 0, nums.length-1);
    }
    private int kThPartition(int[] nums, int k, int l, int r) {
        int left = l;
        int right = r;
        int key = nums[l];

        while (l < r) {
            while (nums[r] <= key && l < r) r--;
            nums[l] = nums[r];
            while (nums[l] >= key && l < r) l++;
            nums[r] = nums[l];
        }

        if (l == k - 1) {
            return key;
        } else if (l >= k - 1) {
            return kThPartition(nums, k, left, l-1);
        } else {
            return kThPartition(nums, k, l + 1, right);
        }
    }
}

