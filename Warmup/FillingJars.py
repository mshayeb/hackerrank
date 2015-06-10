if __name__ == '__main__':
    n,m = map(int, raw_input().split())
 
    answer = 0
 
    for _ in xrange(m):
        a, b, k = map(int, raw_input().split())
        answer += (abs(a-b)+1)*k
    print answer//n