package priv.tanzhen.scalastudy

import scala.beans.BeanProperty

/**
 * Created by TanZhen on 2016/9/28.
 */

/** BeanProperty有getName，无setName **/
class Student private(@BeanProperty val name: String, @BeanProperty var age: Int, var sex:Int) {
  private[this] var value = 0 /** 对象私有，不生成get和set **/
  private var ID = 0 /** 类私有**/

  /*def this(age: Int){
    this() /**Call主构造器**/
    this.age = age
  }*/

  println("Student Construct...." +name + age)

  def compare(s: Student): Unit ={
    s.ID = 1
    value = 2
  }
  def increament() {
    age += 1
  }

}
