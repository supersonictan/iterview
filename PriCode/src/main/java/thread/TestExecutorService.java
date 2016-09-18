package thread;

import java.util.concurrent.*;

/**
 * Created by tanzhen on 2016/6/21.
 */
public class TestExecutorService {

    private static BlockingQueue queue = new ArrayBlockingQueue(1000);
    private static ExecutorService executorService = new ThreadPoolExecutor(1, 1,100, TimeUnit.SECONDS, queue, new ThreadPoolExecutor.DiscardOldestPolicy());


    public static void main(String[] args) {
        /***
         * 导致问题原因：
         *  1.没有主动的cancel超时任务
         *  2.线程池太小，应该设置固定线程数。
         */
        System.out.println("queue size:" + queue.size());
        long st = System.currentTimeMillis();
        Future f1 = executorService.submit(new ThreadTest());
        Future f2 = executorService.submit(new ThreadTest());
        Future f3 = executorService.submit(new ThreadTest());

        try {
            System.out.println("queue size:" + queue.size());
            f1.get(1000,TimeUnit.MILLISECONDS);
            f2.get();
            f3.get();
        } catch (InterruptedException e) {
            e.printStackTrace();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (TimeoutException e) {
            System.out.println("timeout cancel:" + f1.cancel(true));
        }


        /*for(int i=0;i<3;i++){
            Future future = executorService.submit(new ThreadTest());
            try {
               System.out.println( "cost-time:" + (System.currentTimeMillis() - st) + " " + future.get(10000,TimeUnit.MILLISECONDS));
                //System.out.println( "cost-time:" + (System.currentTimeMillis() - st) + " " + future.get());
            } catch (InterruptedException e) {
                e.printStackTrace();
            } catch (ExecutionException e) {
                e.printStackTrace();
            } catch (TimeoutException e) {
                System.out.println("timeout...cannelStatus:"+future.cancel(true));

            }
        }*/

    }
}
class ThreadTest implements Callable<Integer>{

    @Override
    public Integer call() throws Exception {
        System.out.println(Thread.currentThread().getName() + " start.");

        Thread.sleep(5000);
        System.out.println(Thread.currentThread().getName() + " end");
        return 3;
    }
}
