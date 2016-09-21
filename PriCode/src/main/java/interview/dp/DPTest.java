package interview.dp;

import java.util.*;

/**
 * Created by tanzhen on 2016/9/8.
 *
 * 1. 求字符串内不包含重复字符的最长子串 sstrWithoutChar_ON2, 最好的 lengthOfLongestSubstring
 * 2. 最长公共子序列 LCS
 * 3. 最长递增子序列 LIS
 * 4. 最长回文子串 longestPalindromeDP1
 * 5. 求数对只差对大值 getMaxDiff
 */
public class DPTest {





    /**5.求数对只差对大值**/
    public static int getMaxDiff(int[] arr){
        if (arr == null || arr.length == 0){ return 0; }

        int[] maxDiff = new int[arr.length]; //i之前的最大差
        int[] max = new int[arr.length];//存储i之前的最大值

        int left = 0; //左边最大数
        int right = 0;

        max[0] = arr[0];

        for (int i=1; i<arr.length; i++){
            maxDiff[i] = Math.max(maxDiff[i-1], max[i-1]-arr[i]);
            max[i] = Math.max(max[i-1], arr[i]);

            if (maxDiff[i-1] <= (max[i-1]-arr[i])){
                right = arr[i];
            }
            if (max[i-1] <= arr[i]){
                left = arr[i];
            }
        }

        System.out.println("左边最大:" + left + "--右边值:" + right);
        return maxDiff[arr.length-1];
    }
    
    /**4 最长回文子串**/
    public static String longestPalindromeDP1(String s) {
        int len = s.length();
        int longestBegin = 0;
        int maxLen = 1;
        boolean[][] isPalindrome = new boolean[len+1][len+1];

        for(int i=0; i<len; i++) { isPalindrome[i][i] = true; }
        for(int i=0; i<len-1; i++) {
            if(s.charAt(i) == s.charAt(i+1)) {
                isPalindrome[i][i+1] = true;
                longestBegin = i;
                maxLen = 2;
            }
        }
        for(int l = 2; l <= len; l++) {          // 回文子串的长度
            for(int i = 0; i < len-l+1; i++) {   // 回文子串的开始位置
                int j = i+l-1;                  // 回文子串的结束位置
                if(isPalindrome[i+1][j-1] && s.charAt(i) == s.charAt(j)) {
                    isPalindrome[i][j] = true;
                    longestBegin = i;
                    maxLen = l;
                }
            }
        }
        return s.substring(longestBegin, longestBegin+maxLen);
    }

    public static void printMatrix(int[][] matrix){
        for(int i=0;i<matrix.length;i++){
            for (int j=0;j<matrix[0].length;j++){
                System.out.print(matrix[i][j] +",");
            }
            System.out.println();
        }
    }

    /** 1.求字符串内不包含重复字符的最长子串 最优 dp**/
    public static int lengthOfLongestSubstring (String s) {
        Map<Character,Integer> map = new HashMap<Character,Integer>();
        int maxLength = 0;
        int now = 0;
        for(int i = 0; i < s.length(); i++){
            if(map.containsKey(s.charAt(i))){
                now = Math.max(map.get(s.charAt(i))+1,now);
                if((i-now+1)>maxLength){
                    maxLength=i-now+1;
                }
            }else{
                if((i-now+1)>maxLength){
                    maxLength=i-now+1;
                }
            }
            map.put(s.charAt(i), i);
        }
        return maxLength;
    }
    /** 1.求字符串内不包含重复字符的最长子串 n^2复杂**/
    public static int strWithoutChar_ON2(String str){
        if(str==null||str.equals("")){
            return 0;
        }
        Set<Character> set = new HashSet<Character>();
        int maxLength=0;
        int pre=0;
        int after=0;
        while(after<str.length()){
            if(!set.contains(str.charAt(after))){
                set.add(str.charAt(after));
                after ++;
            }else{
                set.clear();
                if((after-pre)>maxLength){
                    maxLength=after-pre;
                }
                pre ++;
                after=pre;
            }
        }

        if((after-pre)>maxLength){
            maxLength=after-pre;
        }
        return maxLength;
    }

    /** 4.LCS **/
    public static void LCS(String strA, String strB){
        char[] A = strA.toCharArray();
        char[] B = strB.toCharArray();
        int[][] result = new int[A.length + 1][B.length + 1];//result[0][0]是初始条件

        //i和j都是result的下标
        for (int i=1; i<A.length+1; i++){
            for (int j=1; j<B.length+1; j++){
                if(A[i-1] == B[j-1]){
                    result[i][j] = result[i-1][j-1] +1;
                }else if (result[i-1][j] >= result[i][j-1]){
                    result[i][j] = result[i-1][j];
                }else {
                    result[i][j] = result[i][j-1];
                }
            }
        }
        printLCS(result, A, B, A.length, B.length);
    }
    public static void printLCS(int[][] result, char[] x, char[] y, int i, int j){
        if(i ==0 || j ==0){ return ;}
        if (x[i-1] == y[j-1]){
            printLCS(result, x, y, i-1, j-1);
            System.out.print("-" + x[i-1]);
        }else if (result[i-1][j] >= result[i][j-1]){
            printLCS(result, x, y, i-1 ,j);
        }else {
            printLCS(result, x, y, i, j-1);
        }
    }

    /** 3. LIS 最长递增子序列 **/
    public static int LIS(int[] arr){
        int L[] = new int[arr.length];
        int max = -1;
        int beginIdx = -1;
        int endIdx = -1;
        for (int j =1; j < arr.length; j++){ //当前要求的下标
            for (int i=0; i<j; i++){ //获得之前最大的L
                if(arr[j] > arr[i] && L[j] < (L[i]+1)){
                    L[j] = L[i] + 1;
                    if(L[j] > max){
                        max = L[j];
                        beginIdx = i;
                        endIdx = j;
                    }
                }
            }
        }
        System.out.println(beginIdx + "--" + endIdx);
        System.out.println(max +1);
        return max +1;
    }

    public static void main(String[] args) {
        //LCS("BDCABA", "ABCBDAB");
        //LIS(new int[]{9, 10, 5, 6, 7, 1, 2, 8});

        int[] arr = {2, 4, 1, 16, 7, 5, 11, 9};
        System.out.println(getMaxDiff(arr));
    }

}
