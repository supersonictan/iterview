package priv.tanzhen.scalastudy

/**
 * Created by TanZhen on 2016/9/29.
 */
object Collection2 {

  val elem = "SINA"
  val list1: List[String] = "Google" :: "Baidu" :: Nil
  val list2: List[String] = "Taobao" :: "JD" :: Nil
  println(list1 :: list2)   //List(List(Google, Baidu), Taobao, JD)
  println(elem :: list1)    //List(SINA, Google, Baidu)
  println(list1 ::: list2)  //List(Google, Baidu, Taobao, JD)
  println(list1.:::(list2)) //List(Taobao, JD, Google, Baidu)
  println(list1 :+ elem)    //List(Google, Baidu, SINA)

  val result = 1 to 5 reduceLeft(_ * _)
  println(result)

  val f: PartialFunction[Char, Int] = {case '+' => 1; case _ => 0}
  println(f('_'))

  def main(args: Array[String]) {

  }
}
