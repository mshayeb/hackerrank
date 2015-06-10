# There are two methods:

# A) generate all fibonacci numbers up to N and check if the candidates are in this set.

# B) There is a mathematical function that can prove whether a number is in the Fibonacci sequence in sqrt(N) time. I am not going to explain this here.

def getFibo(N):
    v = [1,2]
    while v[-1] < N:
        v.append(v[-1]+v[-2])
     
    return set(v)
 
def isFibo(fiboSet, value):
    if value in fiboSet:
        return "IsFibo"
    return "IsNotFibo"
 
if __name__ == '__main__':
    t = input()
    values = []
    for _ in xrange(t):
        values.append(input())
     
    fiboSet = getFibo(max(values))
     
    for value in values:
        print isFibo(fiboSet, value)

