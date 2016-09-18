package interview;

/**
 * Created by tanzhen on 2016/7/10.
 */
public class ZuHe {

    static String[] str  = {"A", "B", "C"};

    public static void main(String[] args) {
        int nCnt = str.length; //循环0-2，让1分别左移0、1、2位
        // nBit从0开始循环，每nBit++都对应二进制+1
        // （不同的二进制代表不同的组合正好对应所有组合形式）
        int nBit = 1<<nCnt;
        for(int bit=1;bit<nBit;bit++){ //从1开始迭代，直到所有解的空间2^n
            for(int cnt = 0; cnt<nCnt; cnt++){//代表左移（0-2）
                if((bit & (1<<cnt)) != 0){//(1<<cnt)eg:001, 010, 100
                    System.out.print(str[cnt]);
                }
            }
            System.out.println("");
        }
    }
}
