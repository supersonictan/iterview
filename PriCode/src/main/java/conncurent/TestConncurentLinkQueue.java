package conncurent;

import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;
import java.util.concurrent.Executor;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Created by tanzhen on 2016/6/9.
 */
public class TestConncurentLinkQueue {
    private static Queue<Integer> queue = new ConcurrentLinkedQueue<Integer>();
    private static ExecutorService executorService = Executors.newFixedThreadPool(10);

    public static void main(String[] args) {
        for(int i=1;i<100;i++){
            queue.add(i);
        }
        

    }



}
