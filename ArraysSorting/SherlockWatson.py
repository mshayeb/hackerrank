# I could rotate the array before going into the test cases, but I can simply rotate the array on the fly by adding the rotation to the element index.

if __name__ == '__main__':
    n,k,q = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    for _ in xrange(q):
        x = int(raw_input())
        print arr[(x-k)%n]