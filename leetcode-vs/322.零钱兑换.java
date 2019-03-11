import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=322 lang=java
 *
 * [322] 零钱兑换
 *
 * https://leetcode-cn.com/problems/coin-change/description/
 *
 * algorithms
 * Medium (28.71%)
 * Total Accepted:    6K
 * Total Submissions: 20.8K
 * Testcase Example:  '[1,2,5]\n11'
 *
 * 给定不同面额的硬币 coins 和一个总金额
 * amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
 * 
 * 示例 1:
 * 
 * 输入: coins = [1, 2, 5], amount = 11
 * 输出: 3 
 * 解释: 11 = 5 + 5 + 1
 * 
 * 示例 2:
 * 
 * 输入: coins = [2], amount = 3
 * 输出: -1
 * 
 * 说明:
 * 你可以认为每种硬币的数量是无限的。
 * 
 */
class Solution {
    public int coinChange(int[] coins, int amount) {
        /**
         * dp[i]表示装满i需要最少硬币数
         * https://www.cnblogs.com/Kalix/p/7622102.html
         * https://blog.csdn.net/tc_to_top/article/details/52346836
         * https://www.cnblogs.com/jbelial/articles/2116074.html
         * 完全背包方程: for i=1..N for v=0..V f[v]=max{f[v],f[v-c[i]]+w[i]};
         */
        int[] dp = new int[amount + 1];

        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int c : coins) {
            for (int j = 1; j <= amount; j++) {
                if (j >= c && dp[j-c] != Integer.MAX_VALUE) {
                    dp[j] = Math.min(dp[j], dp[j - c] + 1);
                }
            }
        }

        if (dp[amount] == Integer.MAX_VALUE) {
            return -1;
        }
        return dp[amount];
    }
}

