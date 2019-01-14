package interview.ali_2019;


/*
* 300. 最长上升子序列[中等]: int lengthOfLIS(int[] nums)
* 673. 最长递增子序列的个数[中等]: int findNumberOfLIS(int[] nums)
* 674. 最长连续递增序列[简单]: int findLengthOfLCIS(int[] nums)
* 121. 买卖股票的最佳时机[简单]: int maxProfit(int[] prices)
* 70. 爬楼梯[简单]: int climbStairs(int n)
*
* */


public class DP {

    public static void main(String[] args) {
        DP d = new DP();
        int[] test = {10,9,2,5,3,7,101,18};
        System.out.println(d.lengthOfLIS(test));
    }

    // 300. 最长上升子序列
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

    // 673. 最长递增子序列的个数
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

    // 674. 最长连续递增序列
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
