package interview.bit;

/**
 * Created by tanzhen on 2016/8/15.
 */
public class BitTest {

    /**
     * 1.判断一个数是否为2的n次方，isPower
     * 2.求一个数的二进制形式中，1的个数。getOneNum
     */


    /**
     * 二进制的形式只能有一个1。
     * 2^n意味着1向左移n位。n&(n-1)==0才行.O(1)
     */
    public static boolean isPower(int n){
        if(n < 1) return false;
        if(n == 1) return true;
        int k = n & (n-1);
        if(k==0){ return true;}
        else {return false;}

    }

    /**
     * 思路：每次n&（n-1）是消除掉现有最后一个的1。
     * 可以用O(n)遍历，也可以用O(m)，m是1的个数
     * 注意负数
     */
    public static int getOneNum(int n){
        int count = 0;
        while(n!=0){
            n = n & (n-1);
            count++;
        }
        return count;
    }


    public static void main(String[] args) {
        getOneNum(0);
        getOneNum(4);
        getOneNum(10);
        getOneNum(13);
        getOneNum(2047);
    }
}
