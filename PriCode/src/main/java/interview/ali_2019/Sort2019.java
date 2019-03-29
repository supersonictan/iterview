package interview.ali_2019;

/*
 * 153. 旋转数组最小值，有重复数[中]
 * 154. 旋转数组最小值，有重复数[难]
 * 215. 数组中的第K个最大元素[中]
 * 414. 第三大的数[简单]
 * 704. 二分查找,不存在返回-1[简单]
 * 33. 旋转排序数组搜索target[中等]
 *
 *
 * TODO:347. 前K个高频元素[中]
 * TODO:35. 搜索插入位置
 */

public class Sort2019 {
    int[] arr = {1,2,3,4,5,6,8,9,10,7};

    // 快排
    public void quickSort(int low, int high) {
        while (low < high) {
            int mid = partition(low, high);
            quickSort(low, mid + 1);
            quickSort(mid + 1, high);
        }
    }
    public int partition(int low, int high) {
        int key = arr[low];

        while (low < high) {
            while (low < high && arr[high] >= key) high--;
            arr[low] = arr[high];
            while (low < high && arr[low] <= key) low++;
            arr[high] = arr[low];
        }
        arr[low] = key;

        return low;
    }

    // 215. 数组中的第K个最大元素[中]
    public int findKthLargest(int[] nums, int k) {
        return partition_215(nums, k, 0, nums.length - 1);
    }
    public int partition_215(int[] nums, int k, int l, int r) {
        int left = l;
        int right = r;
        int key = nums[l];

        while (l < r) {
            while (l < r && nums[r] <= key) r--;
            nums[l] = nums[r];
            while (l < r && nums[l] >= key) l++;
            nums[r] = nums[l];
        }

        if (l == k - 1) {
            return key;
        } else if (l > k - 1) {
            return partition_215(nums, k, left, l - 1);
        } else {
            return partition_215(nums, k, l + 1, right);
        }
    }

    // 414. 第三大的数[简单]
    public int thirdMax(int[] nums) {
        Integer max1 = null;
        Integer max2 = null;
        Integer max3 = null;

        for (Integer n : nums) {
            if (n.equals(max1) || n.equals(max2) || n.equals(max3)) continue;

            if (max1 == null || n > max1) {
                max3 = max2;
                max2 = max1;
                max1 = n;
            } else if (max2 == null || n > max2) {
                max3 = max2;
                max2 = n;
            } else if (max3 == null || n > max3) {
                max3 = n;
            }
        }

        return max3 == null ? max1 : max3;
    }
    // TODO：347. 前K个高频元素[中]

    // TODO：35. 搜索插入位置
    public int searchInsert(int[] nums, int target) {
        return 0;
    }

    // TODO:K路归并

    // 704. 二分查找,不存在返回-1[简单]
    public int search(int[] nums, int target) {
        if (nums.length == 0) return -1;

        int left = 0;
        int right = nums.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }

    // 33/81. 旋转排序数组搜索target[中等]
    public int search33(int[] nums, int target) {
        if (nums.length == 0) return -1;

        int left = 0;
        int right = nums.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (nums[mid] == target) return mid;
            if (nums[left] == target) return left;
            if (nums[right] == target) return right;

            if (nums[left] < nums[mid]) {  // 左边递增
                if (nums[left] < target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else if (nums[mid] < nums[right]) {  // 右边递增
                if (nums[mid] < target && target < nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                left++;
            }
        }
        return -1;
    }

    // 153. 旋转数组最小值，有重复数[中]
    public int findMin(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int left = 0;
        int right = nums.length - 1;
        if (nums[left] < nums[right]) return nums[left];

        while (left < right) {
            int mid = (left + right) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {  // 不能-1因为可能包含最小值
                right = mid;
            } else {
                right--;
            }
        }
        return nums[left];
    }

    // 154. 旋转数组最小值，有重复数[难]
    public int findMin2(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];

        int left = 0;
        int right = nums.length - 1;
        if (nums[left] < nums[right]) return nums[left];

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else if (nums[mid] < nums[right]) {
                right = mid;  // right可能是最小值不能-1
            } else {
                //如果中间和最后相等。怎么查找，主要前后移动方向不确定
                //无法确定的时候，让 右边的值自减就好了
                right--;
            }
        }
        return nums[left];
    }

}
