package interview.sort;

import java.util.*;

/**
 * Created by tanzhen on 2017/9/4.
 */


/*
* 堆排序
* 插入排序
* 冒泡排序
* 快排
* 第k大元素
* 中位数
* 两数之和=给给定数字
* 三数之和:a + b + c = 0
* 拼接最大数：重新排列他们的顺序把他们组成一个最大的整数
* 最接近的三数之和:给一个包含n个整数的数组S, 找到和与给定整数target最接近的三元组，返回这三个数的和。
* 给一个数组，并且数组里面元素的值只可能是0,1,2，然后现在把这个数组排序
* 四数之和:给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)
* 二分查找
* 二分查找第一个出现下标
* 二分查找：找到7,8,9,1,2,3,4,5,6的分段位置
* 二分查找-数组位移
* x的n次幂-nlgn
* 搜索二维矩阵
*
* */
public class AllSort {

    int[] arr = {1,2,3,4,5,6,8,9,10,7};
    public static void main(String[] args) {
        int[] num = {4,5,6,7,0,1,1,1,1,1,2};
        int[][] matrix = {{1,5,10,11,16,23,24,26,29,34,41,48,49,56,63,67,71,74,75},{97,118,131,150,160,182,202,226,251,273,289,310,326,349,368,390,401,412,428},{445,455,466,483,501,519,538,560,581,606,631,643,653,678,702,726,748,766,781},{792,817,837,858,872,884,901,920,936,957,972,982,1001,1024,1044,1063,1086,1098,1111},{1129,1151,1172,1194,1213,1224,1234,1250,1267,1279,1289,1310,1327,1348,1371,1393,1414,1436,1452},{1467,1477,1494,1510,1526,1550,1568,1585,1599,1615,1625,1649,1663,1674,1693,1710,1735,1750,1769}};
        AllSort sort = new AllSort();
        //sort.heapify(num);
        System.out.println(sort.searchMatrix(matrix,1769));
    }


    /*堆排序*/
    public void heapify(int[] A) {
        for(int i = A.length / 2; i >= 0; i--){
            heapify(A, i);
        }
    }
    void heapify(int[] A, int i) {
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        int small = i;
        if(left < A.length && A[left] < A[small]) {
            small = left;
        }
        if(right < A.length && A[right] < A[small]) {
            small = right;
        }
        if(small != i) {
            int tmp = A[small];
            A[small] = A[i];
            A[i] = tmp;
            heapify(A, small);
        }
    }

    /**插入排序**/
    public void insertSort(int[] A) {
        if (A == null || A.length==0) {return ;}
        for (int i=1; i<A.length; i++) {
            for (int j=i; j>0; j--) {
                if (A[j] < A[j-1]){
                    int tmp = A[j];
                    A[j] = A[j-1];
                    A[j-1] = tmp;
                }else{
                    break;
                }
            }
        }
    }
    /*冒泡排序*/
    public void bubbleSort(int[] A) {
        for (int i=A.length-1; i>0; i--){
            for (int j=0; j<i; j++) {
                if (A[j] > A[j+1]) {
                    int tmp = A[j];
                    A[j] = A[j+1];
                    A[j+1] = tmp;
                }
            }
        }
    }

    /*快排*/
    public void quickSort(int low, int high){
        if (low < high) {
            int mid = partition(low,high);
            quickSort(low, mid-1);
            quickSort(mid+1, high);
        }
    }
    public int partition(int low,int high) {
        int key = arr[low];
        while (low<high){
            while (low<high && arr[high] >= key) high--;
            arr[low] = arr[high];
            while (low<high && arr[low] <= key) low++;
            arr[high] = arr[low];
        }
        arr[low] = key;
        return low;
    }

    /*第k大元素*/
    public int kthLargestElement(int k, int[] nums) {
        return kthPartition(nums, 0,nums.length-1,k);
    }
    public int kthPartition(int[] nums, int left, int right, int k) { //倒序
        int i = left;
        int j = right;
        int tmp = nums[i];
        while(i<j){
            while(i<j && tmp>=nums[j]) j--;
            if(i<j){ nums[i]=nums[j]; }
            while(i<j && tmp<=nums[i]) i++;
            if(i<j){ nums[j]=nums[i]; }
        }
        if(i == k -1){
            return tmp;
        }else if(i< k-1){
            return kthPartition(nums,i+1,right,k);
        }else{
            return kthPartition(nums,left,i-1,k);
        }
    }

    /*中位数*/
    public int median(int[] nums) {
        int len = nums.length%2==0?nums.length/2 : nums.length/2+1;
        return medianPartition(nums, 0, nums.length-1, len);
    }
    public int medianPartition(int[] arr, int l, int r, int k) {
        int left = l;
        int right = r;
        int key = arr[left];
        while (left< right) {
            while (left< right && arr[right] >= key) right--;
            if (left<right) arr[left] = arr[right];
            while (left<right && arr[left] <= key) left++;
            if (left< right) arr[right] = arr[left];
        }
        if (left == k-1) return key;
        else if(left< k-1) return medianPartition(arr,left+1, r, k);
        else return medianPartition(arr, l, right-1,k);
    }

    /*两数之和=给给定数字:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target
    * Hash*/
    public int[] twoSum(int[] numbers, int target) {
        // write your code here
        if (numbers == null || numbers.length < 2 ){
            return null;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i=0;i<numbers.length;i++){
            map.put(numbers[i], i);
        }
        int[] res = new int[2];
        for (int i=0; i<numbers.length; i++){
            int need = target - numbers[i];
            if (map.containsKey(need)){
                res[0] = i+1;
                res[1] = map.get(need) + 1;
                break;
            }
        }
        return res;
    }

    /*三数字之和=0
    * O(nlogn)+O(n^2)*/
    public List<List<Integer>> threeSum(int[] numbers) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i=0; i<numbers.length-1;i++) {
            int l = i+1, r=numbers.length-1;
            while (l<r) {
                int sum = numbers[i] + numbers[l] + numbers[r];
                if (sum == 0) {
                    List<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(numbers[i]);
                    tmp.add(numbers[l]);
                    tmp.add(numbers[r]);
                    if (!res.contains(tmp)) res.add(tmp);
                }
                if (sum <0) l++;
                else r--;
            }
        }
        return res;
    }

    /*拼接最大数：重新排列他们的顺序把他们组成一个最大的整数
     * s1比s2小的话返回负数,s1排在s2前面.那第一个s2comparetos1,s2比s1大
     * */
    public String largestNumber(int[] num) {
        if(num == null || num.length == 0) return "";
        String[] strs = new String[num.length];
        for(int i = 0; i < num.length; i++){
            strs[i] = String.valueOf(num[i]);
        }
        Arrays.sort(strs,new NumberCompare());
        StringBuilder sb = new StringBuilder();
        for(String i : strs) {
            sb.append(i);
        }
        String res =  sb.toString();
        int index = 0;
        while(index < res.length() && res.charAt(index) == '0'){
            index++;
        }
        if(index == res.length()) return "0";
        return res.substring(index);
    }
    class NumberCompare implements Comparator<String>{
        @Override
        public int compare(String s1, String s2){
            return (s2+s1).compareTo(s1+s2);
        }
    }

    /*最接近的三数之和:
    给一个包含n个整数的数组S, 找到和与给定整数target最接近的三元组，返回这三个数的和*/
    public int threeSumClosest(int[] numbers, int target) {
        Arrays.sort(numbers);
        int res = Integer.MAX_VALUE;
        for (int i=0; i<numbers.length-1; i++) {
            int j = i+1, k = numbers.length-1;
            while (j<k) {
                int sum = numbers[i] + numbers[j] + numbers[k];
                res = Math.abs(target-sum) < Math.abs(res-target) ? sum : res;
                if (sum < target) j++;
                else if(sum> target)k--;
                else return sum;
            }
        }
        return res;
    }

    /*O(n)数组里面元素的值只可能是0,1,2，然后现在把这个数组排序*/
    public void sortColors(int[] nums) {
        int left = 0, cur = 0, right = nums.length-1;
        while (cur <= right) {
            if (nums[cur] == 0) swap(nums, left++, cur++);
            else if (nums[cur] == 1) cur++;
            else if (nums[cur] == 2) swap(nums, cur, right--);
        }
    }

    /*四数之和:
    数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)*/
    public List<List<Integer>> fourSum(int[] numbers, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i=0; i<numbers.length; i++) {
            for (int j=i+1; j<numbers.length; j++) {
                int tmp = numbers[i] + numbers[j];
                int k = j+1, l = numbers.length-1;
                while (k<l) {
                    int new_sum = tmp+ numbers[k] + numbers[l];
                    if (new_sum == target) {
                        List<Integer> tmpList = new ArrayList<Integer>();
                        tmpList.add(numbers[i]);
                        tmpList.add(numbers[j]);
                        tmpList.add(numbers[k++]);
                        tmpList.add(numbers[l--]);
                        if (!ret.contains(tmpList)) {
                            ret.add(tmpList);
                        }
                    } else if(new_sum < target) {
                        k++;
                    } else {
                        l--;
                    }
                }
            }
        }
        return ret;
    }

    /*二分查找*/
    public int binarySearch(int[] nums, int target) {
        if (nums == null && nums.length == 0) {
            return -1;
        }
        int begin = 0;
        int end = nums.length-1;
        while (begin < end) {
            int mid = (begin + end) /2;
            if (target == nums[mid]) return mid;
            else if (target > nums[mid]) begin = mid+1;
            else end = mid-1;
        }
        return -1;
    }
    /*二分查找：第一次出现的下标*/
    public int binarySearch_first(int[] nums, int target) {
        int begin = 0;
        int end = nums.length-1;
        int res = -1;
        while (begin<=end) {
            int mid = (begin+end) / 2;
            if (nums[mid] == target) {
                if (res<0) res = mid;
                if (res>0 && mid<res) res = mid;
                end = end-1;
            }else if (nums[mid] > target) {
                end = mid-1;
            } else {
                begin = mid + 1;
            }
        }
        return res;
    }
    /*二分查找-数组位移 5,6,7,8,9,10,1,2,3,4*/
    public static int biSearch_seg(int[] A,int target){
        int left = 0;
        int right = A.length-1;
        while (left<=right) {
            int mid = (left + right) /2;
            if (A[mid] == target) return mid;
            if (A[left] < A[mid]) {//左边递增
                if (target < A[mid] && target > A[left]) {
                    right = mid-1;
                }else {
                    left = mid+1;
                }
            } else if (A[left] > A[mid]) { //右边递增
                if (target > A[mid] && target<A[right]) {
                    left = mid +1;
                }else {
                    right = mid -1;
                }
            } else {
                left++;
            }
        }
        return -1;
    }


    /*位移数组 7,8,9,1,2,3,4,5,6的最小值*/
    public int findMin(int[] num) {
        int left = 0;
        int right = num.length - 1;
        while(left < right){
            int mid = (left + right)/2;
            if(num[mid] > num[right]){
                left = mid + 1;
            } else if(num[mid] < num[left]){
                right = mid;
            } else{
                right--;
            }
        }
        return num[left];
    }
    public int findMin_2(int[] num) {
        if (num[0] < num[num.length-1]) return num[0];
        int left = 0;
        int right = num.length-1;
        while(left < right) {
            int mid = (left+right)/2;
            if(mid-1>=0 && num[mid] < num[mid-1] ){
                return num[mid];
            }
            if(mid+1 <= num.length-1 && num[mid] > num[mid+1]) {
                return num[mid+1];
            }
            if (num[left] < num[mid] ) {
                left = mid+1;
            }
            if (num[mid] < num[right]) {
                right = mid-1;
            }
        }
        return -1;
    }

    /*x的n次幂http://www.cnblogs.com/grandyang/p/4383775.html*/
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double half = myPow(x, n / 2);
        if (n % 2 == 0) return half * half;
        else if (n > 0) return half * half * x;
        else return half * half / x; //取倒数
    }

    /*搜索二维矩阵*/
    public boolean searchMatrix(int[][] m, int target) {
        if (m == null || m.length < 1) return false;
        if (m[0][0] > target || m[m.length-1][m[0].length-1] < target) return false;
        int colLen = m[0].length-1;

        int rowIdx=0, colIdx = 0;
        int l = 0;
        int r = m.length-1;
        while (l<=r) {
            int mid = (l+r)/2;
            if (m[mid][0] == target || m[mid][colLen] == target) return true;
            else if (m[mid][0] <= target && m[mid][colLen] >= target) {
                rowIdx = mid;
                break;
            }
            else if (m[mid][0] > target) r = mid-1;
            else if (m[mid][colLen] < target) l = mid+1;
        }

        l = 0;
        r = m[0].length-1;
        while (l <= r) {
            int mid = (l + r)/2;
            if (m[rowIdx][mid] == target) return true;
            else if (m[rowIdx][mid] > target) r = mid-1;
            else if (m[rowIdx][mid] < target) l = mid +1;
        }
        return false;
    }



    public void swap(int[] arr, int left, int right) {
        int tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
    }
}
