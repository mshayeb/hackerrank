# A subset has no common divisor if the GCD equals 1. There is an interesting fact that leads to my solution: If any subset has GCD 1, any bigger set containing this set will also have GCD 1. Therefore GCD(a,b,c,d) = GCD(GCD(GCD(a,b),c),d). This is easily generated by python reduce.

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
 
def multiple_gcd(numbers):
    return reduce(lambda x,y: gcd(x,y), numbers)
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        values = map(int, raw_input().split())
        if len(values) < 2:
            print "NO"
            continue
        if (multiple_gcd(values) == 1):
            print "YES"
        else:
            print "NO"
            