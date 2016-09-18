package interview.sort;

import java.util.Arrays;

/**
 * Created by tanzhen on 2016/7/9.
 */
public class QuickSort {
    static int[] arr = {8,7,6,9,5,4};
    public static int partition(int low, int high){
        int key = arr[low];
        while(low < high){
            while ( low< high && arr[high] >= key) { high --; }
            arr[low] = arr[high];
            while (low< high && arr[low] >= key) { low++; }
            arr[high] = arr[low];
        }
        arr[low] = key;
        return low;
    }
    public static void sort(int low, int high){
        if(low < high){
            int mid = partition(low,high);
            sort(low, mid-1);
            sort(mid+1, high);
        }
    }

    public static void main(String[] args) {
        String s = "";
        String[] ar = s.split(",");
        System.out.println(Arrays.asList(ar).size());
    }

}
