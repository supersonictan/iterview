package thread;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * Created by Supersonic on 2016/7/20.
 */
public class PrintABC_Lock{
    static Lock lock  = new ReentrantLock();
    static Condition conditionA = lock.newCondition();
    static Condition conditionB = lock.newCondition();
    static Condition conditionC = lock.newCondition();
    volatile char currentThreadName = 'A';

    public static void main(String[] args) {

        PrintABC_Lock ce = new PrintABC_Lock();
        ExecutorService service = Executors.newFixedThreadPool(3);
        service.execute(ce.new A());
        service.execute(ce.new B());
        service.execute(ce.new C());

        service.shutdown();
    }

    private class A implements Runnable{
        public void run() {
            for(int i=0;i<10;i++){
                lock.lock();
                while(currentThreadName != 'A'){
                    try {
                        conditionA.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print("A");
                currentThreadName = 'B';
                conditionB.signal();
                lock.unlock();
            }
        }
    }

    private class B implements Runnable{
        public void run() {
            for(int i=0;i<10;i++){
                lock.lock();
                while(currentThreadName != 'B'){
                    try {
                        conditionB.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print("B");
                currentThreadName = 'C';
                conditionC.signal();
                lock.unlock();
            }
        }
    }

    private class C implements Runnable{
        public void run() {
            for(int i=0;i<10;i++){
                lock.lock();
                while(currentThreadName != 'C'){
                    try {
                        conditionC.await();
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
                System.out.print("C");
                currentThreadName = 'A';
                conditionA.signal();
                lock.unlock();
            }
        }
    }
}

