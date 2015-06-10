# I genuinely don’t like n^2 solutions. They scream for a better way. For this task, I struggled to find a better one. Binary search won’t work because of the possible duplicates. Especially special cases where every element is the same and M is double this element. You have to generate all combinations anyways (which is n^2 pairs).

def icecream(flavors, M):
    for idx in xrange(len(flavors)-1):
        for idx2 in xrange(idx+1, len(flavors)):
            if flavors[idx] + flavors[idx2] == M:
                print idx+1, idx2+1
                return
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        m = input()
        n = input()
        flavors = map(int, raw_input().split())
        icecream(flavors, m)