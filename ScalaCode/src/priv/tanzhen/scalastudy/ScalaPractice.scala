package priv.tanzhen.scalastudy
import java.awt.{Color, Font}
import java.util.{HashMap => JavaHashMap} //重命名
import java.util.{HashMap => _,_} //隐藏成员


/**
 * Created by TanZhen on 2016/9/27.
 */
object ScalaPractice {

  /**
   * Cha12
   * 编写函数values(fun:(Int)=>Int,low:Int,high:Int),
   * 该函数输出一个集合，对应给定区间内给定函数的输入和输出。
   * 比如，values(x=>x*x,-5,5)
   * 应该产出一个对偶的集合(-5,25),(-4,16),(-3,9),…,(5,25)
   */


  /**
   * 如何用reduceLeft得到数组中的最大元素?
   */
  val arr = Array(9,8,7,6,5,4,3,2,1)
  println(arr.reduceLeft((a,b) => if(a>b)a else b))

  /**
   * 用to和reduceLeft实现阶乘函数,不得使用循环或递归
   */
  println(1.to(10).reduceLeft((a,b) => a*b))
  println(1.to(10).reduceLeft(_ * _))

  (1 to -10).foreach(println( _))

  "crazy"*3
  println('9' - '0')

  def main(args: Array[String]) {

  }
}
