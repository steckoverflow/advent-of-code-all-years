#!/usr/bin/env scala
import scala.io.Source

object Main extends App {
  val data = Source.fromFile("8.txt").getLines().toList
  data.foreach {v => println(raw"$v".length) }
  println()
  data.foreach {v => println(v.getBytes("UTF-8").length) }
  // print(data)
}
