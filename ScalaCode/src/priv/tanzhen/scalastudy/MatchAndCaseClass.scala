package priv.tanzhen.scalastudy

/**
 * Created by TanZhen on 2016/9/30.
 */
object MatchAndCaseClass {


  /** case class**/



  /**字符串模式匹配**/
  var sign = -1
  val ch = 9
  var arr = Array(0,1,2)
  var list = List(0,1)
  ch match {
    case '+' => sign = 1
    case '-' => sign = -1
    case _: Int => println("afds") /**类型模式**/
    case x: Int if x > 10 => sign = x.toInt /**守卫**/
    case v => sign = 100 /**赋值给v, _ => 是他的特殊情况**/
  }

  arr match {
    case Array(_) => println("Array(0)")
    case Array(x,y) => println(x + "-" + y)
    case Array(0, _*) => println("0 ...._")
    case _ => println("something else..")
  }
  list match {
    case List(0,_*) => println("start 0")
    case 0 :: tail => println("::")
  }


  println(sign)

  /****/

  def main(args: Array[String]) {

  }

}
