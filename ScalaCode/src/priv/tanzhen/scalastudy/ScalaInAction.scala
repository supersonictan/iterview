package priv.tanzhen.scalastudy
import scala.math._

/**
 * Created by TanZhen on 2016/9/26.
 */
object ScalaInAction {




  /**Curry**/


  def time() = {
    System.nanoTime()
  }

  /**Call by name,指定参数名，可变参数**/
  def delayed(t: => Long, name: String*) = {
    println(t)
    for (n <- name){
      println(n)
    }
  }

  /**参数默认值**/
  def add(a: Int=5, b: Int=7): Int ={
    return a + b
  }

  /**高阶函数——作为值的函数**/
  val num = 3.14
  val fun = ceil _
  def triple(x: Double) = x*3

  /**
   * 高阶函数，参数为函数的函数
   * highOrderFunc1的类型为：(Double => Double) => Double
   */
  def highOrderFunc1(f: Double => Double) = f(0.5)

  /** 高阶函数:函数作为返回值的函数
    * 函数类型：Double => (Double => Double)
    * numBy入参Double，返回一个函数
    * highOrderFun2获得这个返回的函数
    */
  def mulBy(factor: Double) = (x: Double) => factor * x
  val highOrderFun2 = mulBy(5D)
  println(highOrderFun2(20)) //100

  /**
   * 参数类型推断
   * highOrderFunc1知道会传递Double=>Double参数，可以简单写
   * 如果参数在 =>右侧只出现一次，可以用 _替换掉
   * 以上仅在参数类型已知下有效
   */
  highOrderFunc1((x: Double) => 3*x)
  highOrderFunc1((x) => 3*x)
  highOrderFunc1(x => 3*x)
  highOrderFunc1(3 * _)

  def foo(a: Int, b: Int, c: Int) {}


  def main (args: Array[String]): Unit = {

    /**打印星星**/
    (1 to 9).map((x: Int) => "*" * x).foreach((x: String) => println(x))
    (1 to 9).map("*" * _).foreach(println( _))

    /**筛选出偶数**/
    (1 to 9).filter( _ % 2 == 0).foreach(println( _))

    "My name is John".split("").sortWith(_.length < _.length)



    //println(add())
  }

}
