package interview;

/**
 * Created by tanzhen on 2016/7/10.
 */
public class PaiLie {

    public static int[] arr = {1,2,3,4,5};
    public static void swap(int[] arr,int idx1, int idx2){
        int temp = arr[idx1];
        arr[idx1] = arr[idx2];
        arr[idx2] = temp;
    }
    public static void pailie(int[] array, int index){
        if(index == array.length){
            for(int a: array){
                System.out.print(a + " ");
            }
            System.out.println();
        }else {
            for(int i=index; i<array.length;i++){
                //for的效果是 1234,2134,3214,4231,递归控制1之后每一个元素和后面的交换
                swap(array,index,i);
                pailie(array,index+1);//
                swap(array,index,i);
            }
        }
    }

    public static void main(String[] args) {
        pailie(arr,0);
    }
}
