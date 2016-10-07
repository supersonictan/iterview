package priv.tanzhen.scalastudy

import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

/**
 * Created by TanZhen on 2016/9/28.
 */
object Collections {


  val map_1 = Map("Tan" -> 10, "Zhen" -> 20, "Cindy" -> 30)
  val map_2 = Map(("JD",21), ("Sina", 2))
  var map_3 = new mutable.HashMap[String, Int]()
  val map_4 = new mutable.HashMap[String, Int]()
  map_3.put("TanZhen",100)
  map_3 += ("A" -> 101, "B" -> 102)
  map_1.getOrElse("Bob",-1)
  map_1.get("Bob") match {
    case Some(_) => println("Got...")
    case None => println("None")
  }

  println("===================tuple======")
  val tuple_1 = ("tan", "zhen", "Good")
  val tuple_2 = ("100, 100, 100")
  println(tuple_1 _3)

  println("===================================")

  /**初始化，和基本访问**/
  val nums_1 = new Array[Int](10)
  val b = new ArrayBuffer[Int]
  val nums_2 = Array("Hello", "World")
  println(nums_2(0))

  /**变长数组 API**/
  b += (1, 1, 2)      //在 b 后面追加元素
  b ++= Array(1,2,3)  // 追加集合
  b trimEnd(3)        //移除最后3个元素
  b insert(2,6,7,8,9) //在下标2之前插入6,7,8,9
  b remove(2,3)       //移除idx=2 及之后的3个元素
  var a = b toArray   //转化为Array
  var c:mutable.Buffer[Int] = a.toBuffer

  /**遍历数组**/
  for (i <- 0.until(10, 2)) print(i) //步长2
  for (i <- b) print(i + "-")
  println("")

  /**数组转换**/
  val newB_1 = for (i <- b if i%2 != 0) yield 2*i
  val newB_2 = b.filter(x=>x%2!=0).map(x => 2*x)

  var first = true
  val newB_3 = for (i <- 0 to b.length if first||b(i)>0) yield {
    //if (b(i) < 0) first = false; i
  }

  println(newB_1)
  println(newB_2)
  println(b)


  def main(args: Array[String]) {
    val w = Worker.getInstance()

    if (w.isInstanceOf[Employee]){
      println("w is Person or subClass")
      w.say
      val p = w.asInstanceOf[Employee]
      p.say
    }





  }
}
