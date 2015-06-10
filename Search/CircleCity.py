# You have to solve the circle equation M^2 + N^2 = D where M and N are integral numbers. 

from math import sqrt, ceil
 
def isCircleProtected(d, K):
    count = 0
    for m in xrange(int(ceil(sqrt(d)))):
        if sqrt(d - m*m).is_integer():
            count += 4
     
    return count <= K
 
if __name__ == '__main__':
    t = input()
    for _ in range(t):
        d, k = map(int, raw_input().split())
        if (isCircleProtected(d, k)):
            print "possible"
        else:
            print "impossible"