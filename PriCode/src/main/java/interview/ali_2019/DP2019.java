package interview.ali_2019;


/*
*
* 数对只差最大值
* 416. 分割等和子集[中]:将数组分割成两个子集，使得两个子集的元素和相等
* 518. 零钱兑换[中]: 可以凑成总金额的硬币组合数
* 322. 零钱兑换[中]: 使用最少的coins凑成total
* 72. 编辑距离[难]
* 198. [简单]在数组中取出一个或多个不相邻数，使其和最大
* 213. 组中取出一个或多个不相邻数，使其和最大，头尾不能相连
*
* 122. 买卖股票最佳时机II[简单]:尽可能多的交易,计算获取的最大利润 int maxProfit2(int[] prices)
* 62. 矩阵左上角到右下角有多少不同路径[中等]:m*n矩阵从左上角到右下角 int uniquePaths(int m, int n)
* 64. 矩阵左上角到右下角,使得路径和最小[中等]: 从左上角到右下角的最小和路径 int minPathSum(int[][] grid)
* 53. 最大和的连续子数组[简单]: 找到一个具有最大和的连续子数组 int maxSubArray(int[] nums)
* 300. 最长上升子序列[中等]: int lengthOfLIS(int[] nums)
* 673. 最长上升子序列的个数[中等]: int findNumberOfLIS(int[] nums)
* 674. 最长连续递增序列[简单]: int findLengthOfLCIS(int[] nums)
* 121. 买卖股票的最佳时机[简单]: int maxProfit(int[] prices)
* 70. 爬楼梯[简单]: int climbStairs(int n)
*
* */


import java.util.HashMap;
import java.util.Map;

public class DP2019 {

    public static void main(String[] args) {
        DP2019 d = new DP2019();
        int[] test = {10,9,2,5,3,7,101,18};
        System.out.println(d.lengthOfLIS(test));
    }


    // 3. 无重复字符的最长子串[中]
    public int lengthOfLongestSubstring(String s) {
        /**
         * dp[i]：在i字符时最长不重复子串
         * dp[i]有两种情况, 1和2选择一个最小的：
         *      1. [0~i-1]中没有i相同的char
         *      2. s[i]在 [0~i-1]之间出现过
         * 所以 dp[i]=min(i-上次出现idx, dp[i-1]+1)
         */
        if (s.length() == 0) return 0;

        Map<Character, Integer> map = new HashMap<Character, Integer>();
        int[] dp = new int[s.length()];

        map.put(s.charAt(0), 0);
        dp[0] = 1;

        int res = 1;

        for (int i = 1; i < s.length(); i++) {
            if (map.containsKey(s.charAt(i))) {
                int idx = map.get(s.charAt(i));
                dp[i] = Math.min(dp[i - 1] + 1, i - idx);
            } else {
                dp[i] = dp[i - 1] + 1;
            }
            res = Math.max(dp[i], res);

            map.put(s.charAt(i), i);
        }

        return res;
    }

    // ﻿数对只差最大值
    public int getMaxDiff(int[] nums) {
        /**
         * ﻿f[i] = max(f[i-1], m[i-1] - a[i]), m[i] = max(m[i-1],a[i])
         */
        int[] maxDiff = new int[nums.length];
        int[] max = new int[nums.length];
        max[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            maxDiff[i] = Math.max(maxDiff[i - 1], max[i - 1] - nums[i]);
            max[i] = Math.max(max[i - 1], nums[i]);
        }

        return maxDiff[nums.length - 1];
    }

    // 416. 分割等和子集[中]:将数组分割成两个子集，使得两个子集的元素和相等
    public boolean canPartition(int[] nums) {
        /**
         * 01背包：f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}
         * 优化空间复杂度后公式：f[v]=max{f[v],f[v-c[i]]+w[i]};
         */
        int n = nums.length;
        int sum = 0;

        for (int i = 0; i < n; i++) sum += nums[i];

        if (sum % 2 != 0) return false;

        int t = sum / 2;
        int[] dp = new int[t + 1];

        for (int i = 0; i < n; i++) {
            for (int j = t; j >= nums[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - nums[i]] + nums[i]);
            }
        }
        return dp[t] == t;
    }

    // 518. 零钱兑换[中]: 可以凑成总金额的硬币组合数
    public int change(int amount, int[] coins) {
        /**
         * dp[i], 表示总额为i时的方案数
         * dp[i] = Σdp[i - coins[j]], 方案数=总额为i-coins[j]的方案数的加和
         * dp[0] = 1, 表示总额为0时方案数为1
         */
        int[] dp = new int[amount + 1];
        dp[0] = 1;

        for (int c : coins) {
            for (int i = 1; i <= amount; i++) {
                if (i >= c) {
                    dp[i] += dp[i - c];
                }
            }
        }
        return dp[amount];
    }

    // 322. 零钱兑换[中]:使用最少的coins凑成total
    public int coinChange(int[] coins, int amount) {
        /**
         * dp[i]表示装满i需要最少硬币数
         * 方程: dp[i] = Min(dp[i], dp[i-k]+1)
         */
        int[] dp = new int[amount + 1];

        for (int i = 1; i <= amount; i++) {
            dp[i] = Integer.MAX_VALUE;

            for (int c : coins) {
                if (i >= c && dp[i - c] != Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[i - c] + 1);
                }
            }
        }

        return dp[amount] == Integer.MAX_VALUE ? -1 : dp[amount];
    }

    // 72. 编辑距离
    public int minDistance(String word1, String word2) {
        /*
        *
        * if(word1[i] == word2[j]) dp[i][j] = dp[i-1][j-1]
          else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
          画图参考:https://www.cnblogs.com/sumuncle/p/5632032.html
        * */
        int n = word1.length();
        int m = word2.length();

        int[][] dp = new int[n + 1][m + 1];  // 留出开头,以防有空串

        for (int i = 0; i <= n; i++) dp[i][0] = i;
        for (int i = 0; i <= m; i++) dp[0][i] = i;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (word1.charAt(i) == word2.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j];
                } else {
                    dp[i + 1][j + 1] = Math.min(dp[i + 1][j], Math.min(dp[i][j + 1], dp[i][j])) + 1;
                }
            }
        }
        return dp[n][m];
    }

    // 213. 组中取出一个或多个不相邻数，使其和最大，头尾不能相连

    // 198. 在数组中取出一个或多个不相邻数，使其和最大
    public int rob(int[] nums) {
        /*
        * dp[i]，表示到第i个房子时能够抢到的最大金额
        * dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
        * dp[0] = num[0], dp[1] = max(num[0], num[1])
        * */
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
        int[] dp = new int[nums.length];

        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);

        int res = Math.max(dp[0], dp[1]);

        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(nums[i] + dp[i - 2], dp[i - 1]);
            res = Math.max(dp[i], res);
        }
        return res;
    }

    // 122. 买卖股票的最佳时机II[简单]:尽可能多的交易,计算获取的最大利润
    public int maxProfit2(int[] prices) {
        int res = 0;

        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i + 1] - prices[i] > 0) {
                res += prices[i + 1] - prices[i];
            }
        }
        return res;
    }

    // 62. 不同路径[中等]:m*n矩阵从左上角到右下角
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
        return dp[m - 1][n - 1];
    }

    // 64. 最小路径和[中等]: 从左上角到右下角的最小和路径 int minPathSum(int[][] grid)
    public int minPathSum(int[][] grid) {
        /*
        * 使用动态规划，求出左上角到网络中每个点的代价最小路径和，
        * 假设当前要求的是point(i,j)点，
        * 那么它的值就应该是从左上角到它上面那个点point(i-1,j)的路径和，
        * 与从左上角到它左边那个点point(i,j-1)的路径和，两者中的最小值加上它自身的值。
        * 特别地，第一行的最小路径和只能从左边向右移动，
        * 所以grid[0][j] = grid[0][j] + grid[0][j-1]；
        * 第一列的最小路径和只能从上到下移动，所以grid[j][0] = grid[j][0] + grid[j-1][0].
        * */
        int row = grid.length;
        int col = grid[0].length;

        // 初始化行列
        for (int i = 1; i < row; i++) grid[i][0] += grid[i - 1][0];
        for (int i = 1; i < col; i++) grid[0][i] += grid[0][i - 1];

        for (int i = 1; i < row; i++) {
            for (int j = 1; j < col; j++) {
                grid[i][j] = grid[i][j] + Math.min(grid[i - 1][j], grid[i][j - 1]);
            }
        }
        return grid[row-1][col-1];
    }

    // 53. 最大子序和[简单]: 找到一个具有最大和的连续子数组
    public int maxSubArray(int[] nums) {
        /*
        * sum[i] 表示以 i 元素结尾的最大和
        * max[i] 表示到 i 为止的最大和
        * TODO:可以优化空间复杂度
        * */
        if (nums.length == 0) return 0;

        int[] sum = new int[nums.length];
        int[] max = new int[nums.length];
        sum[0] = nums[0];
        max[0] = nums[0];

        for (int i = 1; i < nums.length; i++) {
            sum[i] = Math.max(sum[i - 1] + nums[i], nums[i]);
            max[i] = Math.max(max[i - 1], sum[i]);
        }
        return max[nums.length - 1];
    }

    // 300. 最长上升子序列[中等]
    public int lengthOfLIS(int[] nums) {
        /*
        * i指针不断后移，dp[]记录以 i 结尾的最长上升序列, notice: 非全局最长
        * 对于每个遍历到的数字i，我们再遍历其之前的所有数字j......
        * */
        if (nums.length == 0) return 0;
        int resVal = 1;
        int[] dp = new int[nums.length];

        for (int i = 0; i < nums.length; i++) dp[i] = 1;

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j] && dp[j] + 1 > dp[i]) dp[i] = dp[j] + 1;
            }
            resVal = Math.max(resVal, dp[i]);
        }
        return resVal;
    }

    // 673. 最长递增子序列的个数[中等]
    public int findNumberOfLIS(int[] nums) {
        /*
        * dp[]记录以 i 结尾的递增序列长度
        * cnt[] 记录 i 结尾的 最长序列个数
        * 对每遍历到的 i，遍历之前的所有元素 j
        *
        * */
        if (nums.length == 0) return 0;

        int res = 0;
        int max_len = 1;

        int[] dp = new int[nums.length];
        int[] cnt = new int[nums.length];

        for (int i = 0; i < nums.length; i++) dp[i] = 1;
        for (int i = 0; i < nums.length; i++) cnt[i] = 1;

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j] && dp[j] + 1 > dp[i]) {  // 找到新的最长seq
                    dp[i] = dp[j] + 1;
                    cnt[i] = cnt[j];
                } else if (nums[i] > nums[j] && dp[j] + 1 == dp[i]) {
                    cnt[i] += cnt[j];
                }
            }
            max_len = Math.max(max_len, dp[i]);
        }

        for (int i = 0; i < nums.length; i++) {
            if (dp[i] == max_len) res += cnt[i];
        }

        return res;
    }

    // 674. 最长连续递增序列[简单]
    public int findLengthOfLCIS(int[] nums) {
        if (nums.length == 0) return 0;
        int result = 1, tmp = 1;

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                tmp++;
                if (tmp >= result) result = tmp;
            } else {
                tmp = 1;
            }
        }

        return result;
    }

    // 121. 买卖股票的最佳时机[简单]
    public int maxProfit(int[] prices) {
        /*
        * O(n)
        * 保存之前的最低价、result
        * 指针每次后移, 计算当前结果、更新最小值
        * */
        if (prices.length == 0) return 0;

        int minPrice = prices[0];
        int result = 0;

        for (int i = 1; i < prices.length; i++) {
            result = Math.max(result, prices[i] - minPrice);
            minPrice = Math.min(minPrice, prices[i]);
        }
        return result;
    }

    // 70. 爬楼梯[简单]
    public int climbStairs(int n) {
        if (n == 0 || n == 1 || n == 2) return n;

        int[] r = new int[n + 1];
        r[1] = 1;
        r[2] = 2;

        for (int i = 3; i < n+1; i++) {
            r[i] = r[i - 1] + r[i - 2];
        }
        return r[n];
    }


}
