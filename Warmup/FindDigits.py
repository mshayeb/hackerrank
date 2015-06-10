# Just follow the problem description. The problem can be optimized by creating a map of digits and their counts.
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        a = input()
        count = 0
        for i in list(str(a)):
            if int(i) != 0 and a % int(i) == 0:
                count += 1
        print count