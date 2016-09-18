package designPatterns;

import java.util.concurrent.Callable;

/**
 * Created by tanzhen on 2016/6/22.
 */
public class TestSingleton {

    public static void main(String[] args) {
        new Thread(new MyThread()).start();
        new Thread(new MyThread()).start();
        new Thread(new MyThread()).start();
    }

}

class MyObject{
    /***
     * 饿汉模式:
     *  缺点是不能有其他实例变量，因为getInstance没有同步
     */
    private static MyObject myObject = new MyObject();
    private MyObject(){}
    public static MyObject getInstance(){
        return myObject;
    }
}

//懒汉模式
class MySingleton{
    private volatile static MySingleton mySingleton;
    private MySingleton(){}
    public static MySingleton getInstance() throws InterruptedException {
        if(mySingleton == null){
            synchronized (MySingleton.class){
                if(mySingleton == null){
                    Thread.sleep(3000); //会出现非单例情况
                    mySingleton = new MySingleton();
                }
            }
        }
        return mySingleton;
    }
}

//使用static方式
class Singleton_static {
    private static Singleton_static instance = null;
    private Singleton_static(){}
    static {
        instance = new Singleton_static();
    }
    public static Singleton_static getInstance(){
        return instance;
    }
}

class MyThread implements Runnable{

    @Override
    public void run() {
        try {
            System.out.println(MySingleton.getInstance().hashCode());
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}