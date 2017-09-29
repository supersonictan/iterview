package interview.dp;

/**
 * Created by ZeYu
 * Date: 2017/9/29.
 * Time: 17:59.
 * DESC: say something
 */
public class DP_new {

    public static void main(String[] args) {

    }


    /*最长公共子序列LCS--O(mn)*/
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
}
