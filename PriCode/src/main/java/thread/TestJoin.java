package thread;

/**
 * Created by tanzhen on 2016/6/20.
 */
public class TestJoin{

    public static void main(String[] args) throws InterruptedException {
        TxtThread tt = new TxtThread();
        Thread t = new Thread(tt);
        t.start();
        t.join();
        //Thread.sleep(5000);
       /* new Thread(tt).start();
        new Thread(tt).start();
        new Thread(tt).start();*/
        System.out.println("main");

    }
}
class TxtThread implements Runnable {
    int num = 100;
    String str = new String();

    public void run() {

        /*synchronized (str) {
            while (num > 50) {
                try {
                    Thread.sleep(10);
                } catch (Exception e) {
                    e.getMessage();
                }
                System.out.println(Thread.currentThread().getName() + "this is " + num--);
            }
        }*/
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("sleep over");
    }
}
