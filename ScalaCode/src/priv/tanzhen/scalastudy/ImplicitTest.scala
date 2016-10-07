package priv.tanzhen.scalastudy

/**
 * Created by TanZhen on 2016/10/2.
 */
object ImplicitTest {



  //person /**缺失入参：Compiler会自动搜索域内定义的隐式值**/

  def person(implicit name: String) = name

  implicit val p = "tanzhen" /**隐式方法**/
  person

  implicit def int2String(x: Int) = x.toString
  person(123) /**类型错误：Compiler会自动搜索隐式转换函数进行转化 Int=>String**/


  class SwingType{
    def  wantLearned(sw : String) = println("兔子已经学会了"+sw)
  }
  object swimming{
    implicit def learningType(s : AminalType) = new SwingType
  }
  class AminalType
  object AminalType{
    import swimming._
    val rabbit = new AminalType
    rabbit.wantLearned("breaststroke")
  }



  def main(args: Array[String]) {
    //println(person)
    /**使对象能调用类中本不存在的方法**/

  }

}