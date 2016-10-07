package priv.tanzhen.scalastudy

import java.io.{BufferedWriter, PrintWriter, FileInputStream, File}

import scala.io.Source

/**
 * Created by TanZhen on 2016/9/29.
 */
object FileAndRegex {

  /**读取文件**/
  val source = Source.fromFile("D:\\a.txt", "UTF-8")
  val iterator = source.getLines()
  for (l <- iterator) println(l) /**打印每一行**/
  source.getLines().toBuffer /**转化成 Buffer**/
  source.getLines().mkString /**转化成String**/
  source.close()

  /**写文件**/
  val out = new PrintWriter("D:\\test.txt")

  for (i <- 1 to 100) out.println(i)
  out.close()



  val file = new File("D:\\filename")
  val in = new FileInputStream(file)
  val bytes = new Array[Byte](file.length.toInt)
  in.read(bytes)
  in.close()




  def main (args: Array[String]) {

  }
}
