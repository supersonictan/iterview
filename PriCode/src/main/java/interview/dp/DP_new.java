package interview.dp;

import java.util.HashSet;
import java.util.Set;

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
     * 爬楼梯
     * 乘积最大连续子序列
     * 单词切分
     * 200.最长回文子串:给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"
     * **/


    public static void main(String[] args) {
        String s = "ab";
        Set<String> set = new HashSet<String>();
        set.add("a");
        set.add("b");
        String ss = "abb";
        longestPalindrome(ss);
        //System.out.println(wordBreak(s, set));
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
    /*爬楼梯*/
    public int climbStairs(int n) {
        if (n == 0 || n == 1 || n == 2) return n;

        int[] r = new int[n+1];
        r[1] = 1;
        r[2] = 2;
        for (int i = 3; i <= n; i++) {
            r[i] = r[i-1] + r[i-2];
        }
        return r[n];
    }
    /*乘积最大连续子序列*/
    public static int maxProduct(int[] nums) {
        //最大值=max(当前元素，max(当前元素*上一次的最大值，当前元素*上一次的最小值))；
        //最小值=min(当前元素，min(当前元素*上一次的最大值，当前元素*上一次的最小值))；
        if (nums.length==1) return nums[0];
        int res = nums[0];//保存前面最大的
        int max = nums[0];//每一个i都乘,但是res只保存最大的
        int min = nums[0];

        for (int i=1; i<nums.length; i++) {
            int max_tmp = max, min_tmp = min;
            max = Math.max(nums[i], Math.max(nums[i]*max_tmp, nums[i]*min_tmp));
            min = Math.min(nums[i], Math.min(nums[i]*max_tmp, nums[i]*min_tmp));
            res = Math.max(max,res);
        }
        return res;
    }
    /*单词切分*/
    public boolean wordBreak(String s, Set<String> dict) {
        if (s == null || s.length() == 0) return true;

        int maxLength = getMaxLength(dict);
        //前i个字符能不能切分
        boolean[] dp = new boolean[s.length() + 1];

        dp[0] = true;
        for (int i = 1; i < s.length()+1; i++) {
            dp[i] = false;
            for (int j=1; j<=maxLength && j<=i; j++) {
                //如果前半部分不可切分，那不用看后半部分，直接进入下一个循环判断
                if (!dp[i - j]) {
                    continue;
                }
                //前半部分可分割，取出后半部分的字符串，进行遍历判断
                String word = s.substring(i - j, i);//中间段
                if (dict.contains(word)) {
                    //如果存在，则表明此时是可以分割的，直接跳出第二层循环
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.length()];
    }
    private int getMaxLength(Set<String> dict) {
        int maxlenth = 0;
        for(String word : dict) {
            maxlenth = Math.max(maxlenth, word.length());
        }
        return maxlenth;
    }

    /*200.最长回文子串:给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"*/
    public static String longestPalindrome(String s) {
        if (s==null || s.length()==0) return null;
        int[][] dp = new int[s.length()+1][s.length()+1];

        int max_idx = -1;
        for (int i=s.length()-1; i>=0; i--) {
            dp[i][i] = 1;
            for (int j=i+1; j<s.length(); j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    dp[i][j] = dp[i+1][j-1] + 2;
                } else {
                    dp[i][j] = Math.max(dp[i+1][j], dp[i][j-1]);
                }
                System.out.println(i+"," + j + "->" + dp[i][j]);
            }
            max_idx = max_idx > dp[i][s.length()-1] ? max_idx : i;
        }
        System.out.println(dp[0][s.length()-1]);
        return s.substring(max_idx+1, dp[0][s.length()-1]);
    }





}
