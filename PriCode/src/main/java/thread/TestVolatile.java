package thread;

/**
 * Created by tanzhen on 2016/4/27.
 */
public class TestVolatile {

    //public boolean flag = true;

    public String test = "aaa";
    public static void main(String[] args) {

        TestVolatile t = new TestVolatile();
        t.test();
    }
    public void test(){
        Thread t1 = new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                test += "bbb";
                while (true){}
            }
        });

        Thread t2 = new Thread(new Runnable() {
            @Override
            public void run() {
                while (true){
                    System.out.println(test);
                }
            }
        });
        t2.start();
        t1.start();
    }

}
