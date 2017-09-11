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
*
*
* */
public class AllSort {

    int[] arr = {1,2,3,4,5,6,8,9,10,7};
    public static void main(String[] args) {
        int[] num = {2,0,0,1,2,0,2};
        AllSort sort = new AllSort();
        //sort.heapify(num);
        sort.sortColors(num);
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

    /**快排**/
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

    /*最接近的三数之和:给一个包含n个整数的数组S, 找到和与给定整数target最接近的三元组，返回这三个数的和*/
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

    /*O(n)给一个数组，并且数组里面元素的值只可能是0,1,2，然后现在把这个数组排序*/
    public void sortColors(int[] nums) {
        int left = 0, cur = 0, right = nums.length-1;
        while (cur <= right) {
            if (nums[cur] == 0) swap(nums, left++, cur++);
            else if (nums[cur] == 1) cur++;
            else if (nums[cur] == 2) swap(nums, cur, right--);
        }
    }

    /*四数之和:给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)*/
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










    public void swap(int[] arr, int left, int right) {
        int tmp = arr[left];
        arr[left] = arr[right];
        arr[right] = tmp;
    }
}
