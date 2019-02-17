package interview.ali_2019.Practise;

import java.util.HashMap;
import java.util.Map;

public class DPPractise {

    // 3. 无重复字符的最长子串[中]
    public int lengthOfLongestSubstring(String s) {

    }

    // ﻿数对只差最大值
    public int getMaxDiff(int[] nums) {

    }

    // 416. 分割等和子集[中]:将数组分割成两个子集，使得两个子集的元素和相等
    public boolean canPartition(int[] nums) {

    }

    // 518. 零钱兑换[中]: 可以凑成总金额的硬币组合数
    public int change(int amount, int[] coins) {

    }

    // 322. 零钱兑换[中]:使用最少的coins凑成total
    public int coinChange(int[] coins, int amount) {

    }

    // 72. 编辑距离
    public int minDistance(String word1, String word2) {

    }

    // 198. 在数组中取出一个或多个不相邻数，使其和最大
    public int rob(int[] nums) {

    }

    // 53. 最大子序和[简单]: 找到一个具有最大和的连续子数组
    public int maxSubArray(int[] nums) {

    }

    // 300. 最长上升子序列[中等]
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) return 0;

        int[] dp = new int[nums.length];
        int res = 0;

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                dp[i]
            }
        }
    }
}
