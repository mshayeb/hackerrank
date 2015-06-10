# The unfairness is the distance between K elements in a sorted array.

if __name__ == '__main__':
    n = input()
    k = input()
    candies = [input() for _ in range(0,n)]
    candies.sort()
    min_diff = 1000000000
    ## Write code here to compute the answer using (n, k, candies)
 
    for i in xrange(n - k + 1):
        min_diff = min(min_diff, candies[i+k-1] - candies[i])
     
    print min_diff