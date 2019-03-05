package interview.ali_2019;

/*
 * 215. 数组中的第K个最大元素[中]
 * 414. 第三大的数[简单]
 *
 *
 * TODO:347. 前K个高频元素[中]
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





}
