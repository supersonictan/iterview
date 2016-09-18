package commonPool;

import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.PooledObjectFactory;
import org.apache.commons.pool2.impl.DefaultPooledObject;

/**
 * Created by tanzhen on 2016/6/24.
 */
public class MyObjectPoolFactory implements PooledObjectFactory<Person> {

    public PooledObject<Person> makeObject() throws Exception {
        System.out.println("make object");
        Person p = new Person("tanzhen",26,"male");
        return new DefaultPooledObject<Person>(p);
    }

    //链接对象过多会destroy
    public void destroyObject(PooledObject<Person> pooledObject) throws Exception {
        System.out.println("Destroy object...");
        Person p = pooledObject.getObject();
        p = null;
    }

    //调用时机：testOnBorrow || testOnCreate || testOnReturn || testWhileIdle
    public boolean validateObject(PooledObject<Person> pooledObject) {
        System.out.println("Validate Object...");
        return true;
    }

    //激活对象，1.从资源池获取资源时候执行。2.回收资源时根据testWhileIdle 判断是否执行。
    public void activateObject(PooledObject<Person> pooledObject) throws Exception {
        System.out.println("Active object...");
    }

    //“钝化对象”，返还资源池时候调用
    public void passivateObject(PooledObject<Person> pooledObject) throws Exception {
        System.out.println("Passive object...");
    }
}
