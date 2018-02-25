package interview.ali_2018;

import java.util.*;

/**
 *
 * 5.第K大数字
 * 80.中位数
 * 457.经典二分查找问题
 * 14.二分查找:找到target第一次出现的下标
 * 159.寻找旋转排序数组中的最小值
 * 62.旋转排序数组搜索target
 * 28.搜索二维矩阵:每行中的整数从左到右是排序的,每行的第一个数大于上一行的最后一个整数。
 * 38.搜索二维矩阵2:每行中的整数从左到右是排序的,每一列的整数从上到下是排序的,在每一行或每一列中没有重复的整数.
 * 56.两数之和:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target
 * 57.三数之和=target的所有组合
 * 58.四数之和
 * 59.最接近的三数之和
 * 排序只有0,1,2的数组,O(n)
 * 633.找到1~n数字中个一重复的，不排序，空间O(1)
 * 428.x的n次幂O(logn)
 *
 *
 * 两数组交(hash或排序后两个指针)
 * 搜索区间:[5, 7, 7, 8, 8, 10]和目标值target=8(给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置)
 * 最大子数组均值(长度固定)
 * 最大子数组平均值(长度>=k)
 *
 * 拼接最大数：重新排列他们的顺序把他们组成一个最大的整数
 *
 *
 * 689. 两数之和
 */

public class Code2018 {

    // 5.第K大数字
    public int kthLargestElement(int k, int[] nums) {
        return kthPartition(nums, 0, nums.length-1, k);
    }
    public int kthPartition(int[] nums, int left, int right, int k) {
        int i = left;
        int j = right;
        int tmp = nums[i];
        while (i<j){
            while(i < j && tmp >= nums[j]) j--;
            if (i<j) { nums[i] = nums[j]; }
            while (i < j && tmp <= nums[i]) i++;
            if (i<j) { nums[j] = nums[i]; }
        }
        if(i == k - 1) {
            return tmp;
        } else if(i< k-1) {
            return kthPartition(nums, i+1, right, k);
        } else {
            return kthPartition(nums, left, i-1, k);
        }
    }
    // 80.中位数
    public int median(int[] nums) {
        int len = nums.length%2==0?nums.length/2 : nums.length/2+1;
        return medianPartition(nums, 0, nums.length-1, len);
    }
    public int medianPartition(int[] arr, int l, int r, int k) {
        int left = l;
        int right = r;
        int key = arr[left];
        while (left < right) {
            while (left < right && arr[right] >= key) right--;
            if (left < right) arr[left] = arr[right];
            while (left < right && arr[left] <= key) left++;
            if (left < right) arr[right] = arr[left];
        }
        if (left == k-1) {
            return key;
        } else if (left < k-1) {
            return medianPartition(arr, left+1, r, k);
        } else {
            return medianPartition(arr, l, right-1, k);
        }
    }

    // 14.二分查找:找到target第一次出现的下标
    public int binarySearch(int[] nums, int target) {
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
    // 457.经典二分查找问题
    public int findPosition(int[] nums, int target) {
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
    // 159. 寻找旋转排序数组中的最小值
    public int findMin(int[] num) {
        if (num[0] < num[num.length-1]) return num[0];
        int left = 0;
        int right = num.length-1;
        while(left < right) {
            int mid = (left + right) / 2;
            if(mid-1 >= 0 && num[mid] < num[mid-1] ){
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
    // 62.旋转排序数组搜索target
    public int search(int[] A, int target) {
        int left = 0;
        int right = A.length-1;
        while (left<=right) {
            int mid = (left + right) /2;
            if (A[mid] == target) return mid;
            if (A[left] == target) return left;  // [1,2,3]
            if (A[right] == target) return right;
            if (A[left] < A[mid]) {  // 左边递增
                if (target < A[mid] && target > A[left]) {
                    right = mid - 1;
                }else {
                    left = mid + 1;
                }
            } else if (A[left] > A[mid]) { // 右边递增
                if (target > A[mid] && target < A[right]) {
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
    // 28.搜索二维矩阵:每行中的整数从左到右是排序的,每行的第一个数大于上一行的最后一个整数。
    public boolean searchMatrix(int[][] m, int target) {
        if (m == null || m.length < 1) return false;
        if (m[0][0] > target || m[m.length-1][m[0].length-1] < target) return false;
        int colLen = m[0].length - 1;

        int rowIdx = 0, colIdx = 0;
        int l = 0;
        int r = m.length - 1;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (m[mid][0] == target || m[mid][colLen] == target) return true;
            else if (m[mid][0] <= target && m[mid][colLen] >= target) {
                rowIdx = mid;
                break;
            }
            else if (m[mid][0] > target) r = mid-1;
            else if (m[mid][colLen] < target) l = mid+1;
        }

        l = 0;
        r = m[0].length - 1;
        while (l <= r) {
            int mid = (l + r)/2;
            if (m[rowIdx][mid] == target) return true;
            else if (m[rowIdx][mid] > target) r = mid - 1;
            else if (m[rowIdx][mid] < target) l = mid + 1;
        }
        return false;
    }
    // 38.搜索二维矩阵2:每行中的整数从左到右是排序的,每一列的整数从上到下是排序的,在每一行或每一列中没有重复的整数.
    public int searchMatrix2(int[][] matrix, int target) {
        if (matrix.length == 0) return 0;
        int rows = matrix.length;
        int col = matrix[0].length;
        int r = 0;
        int c = col - 1;
        int count = 0;
        while (r < rows && c >= 0) {
            if (target == matrix[r][c]) {
                count++;
                if (r + 1 < rows) {
                    r++;
                } else if (c - 1 > 0) {
                    c--;
                } else {
                    return count;
                }
            } else if (target > matrix[r][c]) {
                r++;
            } else {
                c--;
            }
        }
        return count;
    }

    // 56.两数之和:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target
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
    // 57.三数之和=target的所有组合O(nlogn)+O(n^2)
    public List<List<Integer>> threeSum(int[] numbers) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i = 0; i < numbers.length-1; i++) {
            int l = i + 1, r = numbers.length-1;
            while (l < r) {
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

    // 58.四数之和,
    public List<List<Integer>> fourSum(int[] numbers, int target) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Arrays.sort(numbers);
        for (int i = 0; i < numbers.length; i++) {
            for (int j = i+1; j < numbers.length; j++) {
                int tmp = numbers[i] + numbers[j];
                int k = j+1, l = numbers.length - 1;
                while (k < l) {
                    int new_sum = tmp + numbers[k] + numbers[l];
                    if (new_sum == target) {
                        List<Integer> tmpList = new ArrayList<Integer>();
                        tmpList.add(numbers[i]);
                        tmpList.add(numbers[j]);
                        tmpList.add(numbers[k]);
                        tmpList.add(numbers[l]);
                        if (!ret.contains(tmpList)) {
                            ret.add(tmpList);
                        }
                        k++;
                        l--;
                    } else if (new_sum < target) {
                        k++;
                    } else {
                        l--;
                    }
                }
            }
        }
        return ret;
    }
    // 59.最接近的三数之和
    public int threeSumClosest(int[] numbers, int target) {
        Arrays.sort(numbers);
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < numbers.length - 1; i++) {
            int j = i + 1, k = numbers.length - 1;
            while (j < k) {
                int sum = numbers[i] + numbers[j] + numbers[k];
                res = Math.abs(target-sum) < Math.abs(res-target) ? sum : res;
                if (sum < target) j++;
                else if(sum> target)k--;
                else return sum;
            }
        }
        return res;
    }
    // 排序只有0,1,2的数组,O(n)
    public void sortColors(int[] nums) {
        int left = 0, cur = 0, right = nums.length - 1;
        while (cur <= right) {
            if (nums[cur] == 0) swap(nums, left++, cur++);
            else if (nums[cur] == 1) cur++;
            else if (nums[cur] == 2) swap(nums, cur, right--);
        }
    }
    // 633.找到1~n数字中个一重复的，不排序，空间O(1)
    public int findDuplicate(int[] nums) {
        //若不大于mid的数字个数比mid多，
        // 则重复出现在[low, mid]之间。
        //若不大于mid的数字个数比mid少，
        // 重复出现在后半段中[mid+1，high]
        if (nums == null) return -1;
        int l = 1;
        int r = nums.length - 1;
        while (l < r) {
            int mid = (l+r)/2;
            int cnt = 0;
            for (int i=0;i<nums.length;i++){
                if (nums[i] <= mid) cnt++;
            }
            if (cnt > mid) r = mid;
            else l = mid+1;
        }
        return l;
    }

    // 428.x的n次幂O(logn)
    double myPow(double x, int n) {
        double res = 1.0;
        for (int i = n; i != 0; i /= 2) {
            if (i % 2 != 0) res *= x;  // 整体思想折半,奇数折半后丢了1个,找回来
            x *= x;
        }
        return n < 0 ? 1 / res : res;
    }
}
