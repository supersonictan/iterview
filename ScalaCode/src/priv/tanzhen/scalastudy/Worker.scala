package priv.tanzhen.scalastudy

import priv.tanzhen.scalastudy.Worker

/**
 * Created by TanZhen on 2016/9/29.
 */
class Worker private extends Employee{ /**住构造函数不能被外部访问**/

  var ID: Int = 0
  private var name: String = "" /**私有的get和set，外部不能访问**/
  override def say: Unit ={
    println("I am Worker...")
  }
}
object Worker {

  val instance = new Worker()
  def getInstance(): Worker = {
    instance
  }
  def apply(id: Int): Unit ={

  }
}


