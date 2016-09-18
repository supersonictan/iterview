package commonPool;

import org.apache.commons.pool2.ObjectPool;
import org.apache.commons.pool2.impl.*;

/**
 * Created by tanzhen on 2016/6/24.
 */
public class Main {

    public static void main(String[] args) {
        System.out.println("staart");
        MyObjectPoolFactory poolFactory = new MyObjectPoolFactory();

        GenericObjectPool<Person> objectPool = new GenericObjectPool<Person>(poolFactory);
        objectPool.setMaxTotal(30);
        objectPool.setMaxIdle(8);
        objectPool.setMinIdle(8);
        objectPool.setBlockWhenExhausted(true);
        objectPool.setMaxWaitMillis(1000L);
        objectPool.setTimeBetweenEvictionRunsMillis(2000L);
        objectPool.setSoftMinEvictableIdleTimeMillis(10000L);
        //objectPool.setTestOnBorrow(true);

        try {
            Thread.sleep(10000L);
            System.out.println("Start main");
            Person p = objectPool.borrowObject();
            Person p2 = objectPool.borrowObject();
            Person p3 = objectPool.borrowObject();
            Person p4 = objectPool.borrowObject();
            Person p5 = objectPool.borrowObject();
            System.out.println("Num Active:"+objectPool.getNumActive());
            System.out.println("Num Idl:"+objectPool.getNumIdle());
            objectPool.returnObject(p);
            System.out.println(p);

        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
