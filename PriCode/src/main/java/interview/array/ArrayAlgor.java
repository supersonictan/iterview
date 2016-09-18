package interview.array;

import java.util.*;

/**
 * Created by tanzhen on 2016/8/16.
 */
public class ArrayAlgor {

    public static int[] arr = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19};

    /**
     * 1.求最大子数组之和 findMaxSubseq_2
     * 2.最大子数组之和的下标 findMaxSubSeqIndex
     * 3.数组中最小的K个数
     * 4.数组中重复的数字
     * 5.和为s的两个数字（有序）findTwoNum_SameSum
     * 6.和为s的连续正整数序列（有序）findSubSeq_SameSum
     * 7.在二维数组中查找具体数字 findIn2DimArr
     * 8.替换所有空格 replaceAllBlank
     * 9.找出从1到n中1出现的次数 getNumberOf1
     * 10.在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的。请找出数组中任意一个重复的数字 duplicate
     * 11. 去除已排序数组中的重复元素 removeDuplicates
     */



    public static int removeDuplicates(int[] nums) {
        if (nums.length < 1)
            return nums.length;
        int slow = 1;
        for (int fast = 1; fast < nums.length; fast++) {
            if (nums[fast] != nums[slow - 1]) {
                nums[slow++] = nums[fast];
            }
        }
        return slow;
    }
    public static boolean duplicate(int[] arr){
        if(arr== null || arr.length <= 0){
            return false;
        }
        for(int i = 0; i<arr.length; i++){
            while(arr[i] != i){
                if(arr[i] == arr[arr[i]]){
                    System.out.println(arr[i]);
                    return true;
                    //break;
                } else {
                    int temp = arr[i];
                    arr[i] = arr[temp];
                    arr[temp] = temp;
                }
            }
        }

        return false;
    }



    public class getNumberOf1 {
        public int numberOf1BetweenAndN(int n){
            int number = 0;
            for(int i = 1;i<= n;i++){
                number+=numberOf1(i);
            }
            return number;
        }
        public int numberOf1(int n){
            int number =0;
            while(n!=0){
                if(n %10 == 1)
                    number++;
                n = n/10;
            }
            return number;
        }
    }

    /**
     * 找出数组最小的k个数
     */
    public static void getLeastK(int k, int low, int high){

        int mid = partition(low, high);
        while(mid != k-1){
            if(mid > k-1){
                high = mid - 1;
                mid = partition(low,high);
            }else {
                low = mid +1;
                mid = partition(low, high);
            }
        }
    }
    public static int partition(int low, int high){
        int key = arr[low];
        while(low < high){
            while (low < high && arr[high] >= key){
                high --;
            }
            if(low < high){
                arr[low++] = arr[high];
            }
            while (low<high && arr[low] <= key){
                low ++;
            }
            if(low < high){
                arr[high--] = arr[low];
            }
        }
        arr[low] = key;
        return low;
    }


    public static int getBlankNum(String s){
        return 1;
    }
    public static void replaceAllBlank(String testString){
        if(testString == null || testString.length() <= 0){
            return;
        }
        //字符数组初始长度
        int length = testString.length();
        //字符数组增加长度后
        int newLength = testString.length()+ getBlankNum(testString)*2;
        char[] tempArray = new char[newLength];
        System.arraycopy(testString.toCharArray(), 0, tempArray, 0, testString.toCharArray().length);
        int indexofOriginal = length - 1;
        int indexofNew = newLength -1;
        System.out.println("未替换空格时的字符串：");
        //printArray(testString.toCharArray());
        while(indexofOriginal >=0 && indexofOriginal != indexofNew){
            if(tempArray[indexofOriginal]==' '){
                tempArray[indexofNew--]='0';
                tempArray[indexofNew--]='2';
                tempArray[indexofNew--]='%';
            }else{
                tempArray[indexofNew--]= tempArray[indexofOriginal];
            }
            indexofOriginal--;
        }
        System.out.println("替换空格后的字符串：");
        //printArray(tempArray);
    }

    /**在二维数组中查找具体数字 findIn2DimArr**/
    public static boolean findIn2DimArr(int[] arr,int rows ,int colomns,int number){
        boolean found = false;
        if(arr.length>0 && rows >0 && colomns >0){
            int row = 0;
            int colomn = colomns -1;
            while(row < rows && colomn >=0){
                if(arr[row*colomns +colomn]== number)
                {
                    found = true;
                    break;
                }else if(arr[row*colomns+colomn] >number){
                    --colomn;
                }else
                    ++row;
            }
        }
        return found;
    }

    /**
     * 1.求最大子数组之和 findMaxSubseq_2
     */
    public static int findMaxSubseq(int[] arr){
        int n = arr.length;
        int end[] = new int[n];//包含最后一个的和
        int all[] = new int[n];//最大子数组和
        end[0] = all[0] = arr[0];
        for(int i=1;i<n;++i){
            end[i] = max(end[i-1]+arr[i], arr[i]);
            all[i] = max(end[i], all[i-1]);
        }
        return all[n-1];
    }
    public static int findMaxSubseq_2(int[] arr){
        int n = arr.length;
        int end = arr[0];
        int max = Integer.MIN_VALUE;
        for(int i=1;i<n;++i){
            if(end>0){ end += arr[i]; }
            else { end = arr[i]; }
            if(end > max){ max = end; }
        }
        return max;
    }

    /**
     * 2.最大子数组之和的下标 findMaxSubSeqIndex
     */
    public static int findMaxSubSeqIndex(int[] arr){
        int n = arr.length;
        int end = arr[0];
        int max = Integer.MIN_VALUE;

        int startIdx = 0;
        int endIdx = -1;
        int tempBegin = -1;

        for(int i=1;i<n;i++){
            if(end > 0){
                end += arr[i];
            }else {
                end = arr[i];
                tempBegin = i;
            }
            if(end > max){
                max = end;
                startIdx = tempBegin;
                endIdx = i;
            }
        }
        System.out.println(startIdx + "-->" + endIdx);
        return max;
    }

    /**和为s的两个数字**/
    public static void findTwoNum_SameSum(int[] arr, int specSum){
        int begin = 0;
        int end = arr.length-1;
        while (begin < end){
            int sum = arr[begin] + arr[end];
            if(sum == specSum){
                System.out.println("Find:" + arr[begin] + "--" + arr[end]);
                begin ++;
                end --;
            }else if(sum < specSum){
                begin ++;
            }else {
                end --;
            }
        }
    }

    public static void findSubSeq_SameSum(int[] arr, int s){
        int low = 0;
        int high = 1;
        int half = (s +1) /2; //因为low至少比high少1
        while (low < half && high<arr.length-1){
            int sum = getSum(arr,low,high);
            if(sum == s){
                printArr(arr,low,high);
                low++;
                high++;
            }else if(sum < s){
                high ++;
            }else {
                low ++;
            }
        }
    }
    public static int getSum(int[] arr, int low, int high){
        int sum = 0;
        for(int i=low;i<=high;i++){
            sum += arr[i];
        }
        return sum;
    }
    public static void printArr(int[] arr, int low, int high){
        for(int i=low; i<=high;i++){
            System.out.print(arr[i] + ",");
        }
        System.out.print("\n");
    }


    /**
     * 在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复的次数。请找出数组中任意一个重复的数字。
     */
    public static void findDuplicateNum(){
        for(int i=0;i<arr.length;i++){
            while (arr[i] != i);
        }
    }


    public static void main(String[] args) {
        //int[] arr = {1,-2,3,10,-4,7,2,-5,4};
        //int[] arr = {-9,-5,-2,-6,-10};
        //System.out.println(findMaxSubSeqIndex(arr));
        //System.out.println(findMaxSubseq_2(arr));

        //findSubSeq_SameSum(arr, 210);
        int[] arr = {4,3,2,1,0,4,5,3,6,7};
        duplicate(arr);
    }

    public static int max(int m,int n){
        return m>n?m:n;
    }
}
