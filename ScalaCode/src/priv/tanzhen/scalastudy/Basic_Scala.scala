package priv.tanzhen.scalastudy

/**
 * Created by TanZhen on 2016/9/28.
 */
object Basic_Scala {

  def main(args: Array[String]) {

    var result: Long = 0L

    for(i <- "Hello") {
      //result *= i.toLong
    }

    "Hello".foreach(result *= _.toLong)

    for (i <- 0 to 100 reverse) print("result:"+i)

    def product(s: String): Long = {
      if (s.length == 1)  s.charAt(0).toLong
      else s.take(1).charAt(0).toLong * product(s.drop(1))
    }

/*

    /**在 word被定义时候即被取值**/
    val word_1 = scala.io.Source.fromFile("words").mkString
    /**在 word2被首次调用时候取值 **/
    lazy val word_2 = scala.io.Source.fromFile("words").mkString
    /**每一次word被使用时候取值**/
    def word_3 = scala.io.Source.fromFile("words").mkString
*/

    var r:Int = 1
    val n = 10

    if (n > 3) 3 else()
    for (i <- 1 to n)
      r = r * i

    for (i <- 0 until n)
      Unit

    for (i <- 1 to n if i!=1; j<- 1 to n if i!=j)
      print(10*i + j)

    for {i<- 1 to n
         from=i-4
         j<-from to n}
      print(i + "-" + j + from)


    def sum(args: Int*): Int ={
      var result = 0
      for (arg<- args) result += arg
      result
    }

    val s = sum(1 to 100: _*)

    def procedure() { }


  }

}
