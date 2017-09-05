package interview.sort;

import java.util.Arrays;
import java.util.List;

/**
 * Created by tanzhen on 2017/9/4.
 */


/*
* 堆排序
* 插入排序
* 冒泡排序
* */
public class AllSort {

    int[] arr = {5,4,3,2,1};
    public static void main(String[] args) {
        int[] num = {3,4,5,1,2};
        AllSort sort = new AllSort();
        //sort.heapify(num);
        sort.kthLargestElement(2,num);
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

    /*插入排序*/
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
    public int kthPartition(int[] nums, int left, int right, int k) {
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

    /*公共util*/
    public static void swap(int[] A, int idx1, int idx2) {
        int tmp = A[idx1];
        A[idx1] = A[idx2];
        A[idx2] = tmp;
    }
}
