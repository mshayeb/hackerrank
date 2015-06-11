object Solution extends App {
    
  def fibonacci(x: Int, currX: Int = 1, a1: Int = 0, a2: Int = 1): Int =
    if(x == currX) a1
    else fibonacci(x, currX + 1, a2, a1 + a2)

  println(fibonacci(readInt()))
}
