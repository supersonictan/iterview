package interview.ali_2018_2;

public class AllSort {
    int[] arr = {1,2,3,4,5,6,8,9,10,7};

    // 快排
    public void quickSort(int low, int high) {
        while (low < high) {
            int mid = partition(low, high);
            quickSort(low, mid - 1);
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

    // 5.第K大数字
    public int kthLargestElement(int[] num, int k) {
        return kthPartition(num, 0, num.length - 1, k);
    }
    public int kthPartition(int[] num, int left, int right, int k) {
        int l = left;
        int r = right;
        int key = num[l];
        while (l < r) {
            while (l < r && num[r] <= key) r--;
            num[l] = num[r];
            while (l < r && num[l] >= key) l++;
            num[r] = num[l];
        }
        if (l == k - 1) {
            return key;
        } else if (l < k - 1) {
            return kthPartition(num, l + 1, right, k);
        } else {
            return kthPartition(num, left, l - 1, k);
        }
    }

    // 80.中位数
    public int median(int[] num) {
        int k = num.length / 2 == 0 ? num.length / 2 : num.length / 2 + 1;
        return medianPartition(num, 0, num.length - 1, k);
    }
    public int medianPartition(int[] num, int left, int right, int k) {
        int l = left;
        int r = right;
        int key = num[l];
        while (l < r) {
            while (l < r && num[r] >= key) r--;
            num[l] = num[r];
            while (l < r && num[l] <= key) l++;
            num[r] = num[l];
        }
        if (l == k - 1) {
            return key;
        } else if (l < k - 1) {
            return medianPartition(num, l + 1, right, k);
        } else {
            return medianPartition(num, left, l - 1, k);
        }
    }
}
