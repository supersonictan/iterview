package interview.dp;

/**
 * Created by ZeYu
 * Date: 2017/9/29.
 * Time: 17:59.
 * DESC: say something
 */
public class DP_new {

    /**
     * 最长公共子序列O(mn)
     * 最长公共子串
     * 最长上升子序列:给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度
     * 最长公共前缀
     * 最长上升连续子序列
     * 最长上升连续子序列
     * 最少硬币找零问题
     * 编辑距离
     * **/


    public static void main(String[] args) {
        int[] coins = {2,5,7};
        System.out.println(getChange(coins, 16));
    }


    /*最长公共子序列--O(mn)*/
    public int longestCommonSubsequence(String AStr, String BStr) {
        char[] A = AStr.toCharArray(), B = BStr.toCharArray();
        if (AStr.length() == 0 || BStr.length() == 0) return 0;
        int[][] res = new int[A.length+1][B.length+1];

        for (int i=1; i<A.length+1; i++) {
            for (int j=1; j<B.length+1; j++) {
                if (A[i-1] == B[j-1]) {
                    res[i][j] = res[i-1][j-1] + 1;
                } else {
                    res[i][j] = Math.max(res[i][j-1], res[i-1][j]);
                }
            }
        }
        return res[A.length][B.length];
    }
    /*最长公共子串*/
    public int longestCommonSubstring(String AStr, String BStr) {
        char[] A = AStr.toCharArray(), B = BStr.toCharArray();
        if (A.length == 0 || B.length == 0) return 0;
        int[][] res = new int[A.length+1][B.length+1];
        int resVal = -1;

        for (int i=1; i<A.length+1; i++) {
            for (int j=1; j<B.length+1; j++) {
                if (A[i-1] == B[j-1]) {
                    res[i][j] = res[i-1][j-1] + 1;
                } else {
                    res[i][j] = 0;
                }
                resVal = Math.max(resVal, res[i][j]);
            }
        }
        return resVal;
    }
    /*最长上升子序列*/
    public int longestIncreasingSubsequence(int[] nums) {
        int[] res = new int[nums.length];
        int resVal = 0;
        for (int i=0;i<nums.length;i++) res[i] = 1;
        for (int i=1; i<nums.length; i++) {
            for (int j=0; j<i; j++) {
                //与i之前每一个比较,选一个大的
                if (nums[j] < nums[i])
                    res[i] = Math.max(res[i], res[j]+1);
            }
            resVal = Math.max(res[i], resVal);
        }
        return resVal;
    }
    /*最长公共前缀*/
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        if (strs.length == 1) return strs[0];
        int res = Integer.MAX_VALUE;
        for (int i=0; i<strs.length-1; i++) {
            res = Math.min(res, longestCommonPrefix_cmp(strs[i], strs[i+1]));
        }
        return strs[0].substring(0,res);
    }
    public int longestCommonPrefix_cmp(String a, String b) {
        int count = 0, len = Math.min(a.length(), b.length());
        for (int i=0,j=0; i<len; i++,j++) {
            if (a.charAt(i) != b.charAt(j)) return count;
            count++;
        }
        return count;
    }

    /*最长上升连续子序列*/
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A.length == 0) return 0;
        int[] dp = new int[A.length];
        for (int i=0;i<A.length; i++) dp[i] = 1;
        int maxL = 1;
        for (int i=1; i<A.length; i++) {
            if (A[i-1] < A[i]) {
                dp[i] = dp[i-1] + 1;
            }
            maxL = Math.max(maxL, dp[i]);
        }

        int maxR = 1;
        for (int i=A.length-2; i>=0; i--) {
            if (A[i+1] < A[i]) {
                dp[i] = dp[i+1] + 1;
            }else {
                dp[i] = 1;
            }
            maxR = Math.max(maxR, dp[i]);
        }
        return Math.max(maxL, maxR);
    }
    /*最少硬币找零问题*/
    public static int getChange(int[] coins, int k) {
        if(coins.length==0 || k==0) return 0;
        int[] dp = new int[k+1];

        for (int i=1; i<k+1; i++) {
            int min = Integer.MAX_VALUE-k;//后面可以dp[less_coin] + 1
            for (int j=0; j<coins.length; j++) {
                int less_coin = i-coins[j];
                if (less_coin >= 0) {
                    int min_tmp = dp[less_coin] + 1;
                    if (min_tmp < min) min = min_tmp;
                }
            }
            dp[i] = min;
        }
        return dp[k];
    }
    /*编辑距离*/
    public int minDistance(String word1, String word2) {
        int[][] dp = new int[word1.length()+1][word2.length()+1];

        for (int i=1; i<word1.length()+1; i++) dp[i][0] = i;
        for (int i=1; i<word2.length()+1; i++) dp[0][i] = i;

        for (int i=1; i<word1.length()+1; i++) {
            for (int j=1; j<word2.length()+1; j++) {
                char a = word1.charAt(i-1), b = word2.charAt(j-1);
                if (a==b) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    //"sea""ate"需要和dp[i-1][j-1])比较
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i][j-1], dp[i-1][j-1])) + 1;
                }
            }
        }
        return dp[word1.length()][word2.length()];
    }
}
