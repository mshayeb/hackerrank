# The product a*b (where a+b = k) is maximal, when a is close to b as possible. We can only use integral values, so a and b are rounded halves of k.
def oneOneBars(K):
    half = K//2
    return half * (K-half)
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        k = input()
        print oneOneBars(k)