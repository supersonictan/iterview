package priv.tanzhen.scalastudy

import java.io.{FileInputStream, ObjectInputStream, FileOutputStream, ObjectOutputStream}

/**
 * Created by TanZhen on 2016/9/28.
 */
@SerialVersionUID(42L) class Employee extends Serializable{

  def say: Unit = println("I am Person...")
}
object test{
  val e = new Employee
  val out = new ObjectOutputStream(new FileOutputStream("D:\\test.txt"))
  out.writeObject(e)
  val in = new ObjectInputStream(new FileInputStream("D:\\test.txt"))
  val ee = in.readObject().asInstanceOf[Employee] /**类型转化**/

}


