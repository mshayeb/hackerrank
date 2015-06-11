object Solution extends App {
  
  def pascal(x: Int, acc: List[List[Int]] = List(List(1))): List[List[Int]] = {
    if(x == 1) return acc.reverse
    else pascal(x - 1,
      (0 +: acc.head :+ 0).sliding(2).map(_.sum).toList :: acc)
  }

  println(pascal(readInt()).map(_.mkString(" ")).mkString("\n"))
}
