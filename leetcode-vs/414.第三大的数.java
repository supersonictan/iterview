/*
 * @lc app=leetcode.cn id=414 lang=java
 *
 * [414] 第三大的数
 *
 * https://leetcode-cn.com/problems/third-maximum-number/description/
 *
 * algorithms
 * Easy (30.79%)
 * Total Accepted:    5.9K
 * Total Submissions: 19.1K
 * Testcase Example:  '[3,2,1]'
 *
 * 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
 * 
 * 示例 1:
 * 
 * 
 * 输入: [3, 2, 1]
 * 
 * 输出: 1
 * 
 * 解释: 第三大的数是 1.
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: [1, 2]
 * 
 * 输出: 2
 * 
 * 解释: 第三大的数不存在, 所以返回最大的数 2 .
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: [2, 2, 3, 1]
 * 
 * 输出: 1
 * 
 * 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
 * 存在两个值为2的数，它们都排第二。
 * 
 * 
 */
class Solution {
    public int thirdMax(int[] nums) {
        if (nums.length == 0) return 0;

        Integer max1 = null;
        Integer max2 = null;
        Integer max3 = null;

        for (Integer i: nums) {
            if (i.equals(max1) || i.equals(max2) || i.equals(max3)) continue;

            if (max1 == null || max1 < i) {
                max3 = max2;
                max2 = max1;
                max1 = i;
            } else if (max2 == null || max2 < i) {
                max3 = max2;
                max2 = i;
            } else if (max3 == null || max3 < i) {
                max3 = i;
            }
        }
        return max3 == null ? max1 : max3;
    }
}

