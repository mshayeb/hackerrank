# At first sight this seems like a longest common substring problem. It is actually much easier. You just need to find out if there are two equal letters in both strings A and B.
def twoStrings(s1, s2):
    m1 = set(s1)
    m2 = set(s2)
    if set.intersection(m1,m2):
        return "YES"
    return "NO"
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        first = raw_input()
        second = raw_input()
        print twoStrings(first, second)