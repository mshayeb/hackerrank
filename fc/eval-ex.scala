def f(x: Float, n: Int = 0, currX: Float = 1, currD: Float = 1): Float =
  if(n == 10) 0
  else (currX / currD) + f(x, n + 1, currX * x, currD * (n + 1))
