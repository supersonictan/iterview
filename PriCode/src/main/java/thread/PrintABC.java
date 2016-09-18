package thread;

/**
 * Created by tanzhen on 2016/6/21.
 */
public class PrintABC implements Runnable {
    /***
     * 思路表达：
     *  1.为了控制顺序，每打印一个，需要控制它的prev不在打印，所以需要获得prev的 lock
     *  2.又要保证当前打印的下一个字母也不在打印，所以还需要控制self的lock
     *  3.需要注意JVM的具体实现，比如：
     *      在printA时候，还没a.notify，则b需要等待，这时c已获得b的lock然后等a执行完后c.wait,这时C就可以运行了
     *      所以需要用sleep主动放弃CPU
     */
    public String name;
    Object prev;
    Object self;
    int count = 10;

    public PrintABC(String name, Object prev, Object self){
        this.name = name;
        this.prev = prev;
        this.self = self;
    }

    @Override
    public void run() {
        while (count > 0){
            synchronized (prev){
                synchronized (self){
                    System.out.println(name);
                    count --;
                    self.notify();
                }
                try {
                    prev.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                //} 如果synchronized (self)的结尾在这里，notify会等到wait执行完才释放self锁，那么B不会执行
            }

        }
    }
    public static void main(String[] args) throws InterruptedException {
        Object a = new Object();
        Object b = new Object();
        Object c = new Object();

        PrintABC ta = new PrintABC("A", c, a);
        PrintABC tb = new PrintABC("B", a, b);
        PrintABC tc = new PrintABC("C", b, c);

        new Thread(ta).start();
        Thread.sleep(10);
        new Thread(tb).start();
        Thread.sleep(10);
        new Thread(tc).start();


    }
}
