package interview.ali_2019;


/*
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


public class DP2019 {

    public static void main(String[] args) {
        DP2019 d = new DP2019();
        int[] test = {10,9,2,5,3,7,101,18};
        System.out.println(d.lengthOfLIS(test));
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
