# I love this problem as it is a great reference for other pair solutions. There are choose(n,2) pairs in k elements. This reduces to n*(n-1)/2. The if/else branch is not required, but I like to keep it in to be more verbose.

def main():
    n = input()
    for _ in xrange(n):
        t = input()
        if (t == 1):
            print 0
        else:
            print t*(t-1)/2
             
     
if __name__ == '__main__':
    main()