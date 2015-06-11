def f(coefs: List[Int], powers: List[Int], x: Double) =
  coefs.zip(powers).map { case (c, p) => c * math.pow(x, p) }.sum

def area(coefs: List[Int], powers: List[Int], x: Double) = 
  math.Pi * math.pow(f(coefs, powers, x), 2)

def summation(func: (List[Int], List[Int], Double) => Double,
               upperLimit: Double, lowerLimit: Double, coefs: List[Int],
               powers: List[Int], acc: Double = 0.0): Double =
  if(lowerLimit > upperLimit) acc
  else summation(func, upperLimit, lowerLimit + 0.001, coefs, powers, acc +
    func(coefs, powers, lowerLimit) * 0.001)
