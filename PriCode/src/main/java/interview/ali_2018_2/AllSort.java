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


}
