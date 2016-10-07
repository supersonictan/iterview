package priv.tanzhen.scalastudy

/**
 * Created by TanZhen on 2016/9/29.
 */

class SubClass(name: String, id: Long) extends AbstractClass{
  override val intVal: Int = 0
  override def func1: Unit = {
    println("Call func1......")
  }

  /**使用匿名类**/
  val superObj = new AbstractClass() {
    override def func1: Unit = ()
    override val intVal: Int = 0
  }
}
