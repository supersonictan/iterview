package test;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by tanzhen on 2016/6/2.
 */
public class TestIterator {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);
        list.add(5);
        list.add(6);

        Iterator<Integer> iterator = list.iterator();
        while (iterator.hasNext()){
            int ele = iterator.next();

            if(ele == 2){
                iterator.remove();
                //iterator.remove();
                System.out.println("in 2"+iterator);
                System.out.println("rm "+ele);
            }else {
                System.out.println(iterator);
            }
        }
        for(int a:list){
            System.out.println(a);
        }
    }
}
