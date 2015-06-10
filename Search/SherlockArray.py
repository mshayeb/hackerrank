# I first solved the problem using prefix sums. Afterwards I realized that it can be done without additional space complexity.

def sherlockArray(a):   
    
    left_idx = 0
    right_idx = len(a) - 1
     
    left_sum = a[left_idx]
    right_sum = a[right_idx]
     
    while left_idx != right_idx:
        if left_sum < right_sum:
            left_idx += 1
            left_sum += a[left_idx]
        else:
            right_idx -= 1
            right_sum += a[right_idx]
     
    return left_sum == right_sum
     
if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n = int(raw_input())
        a = map(int, raw_input().split())
        if arraySherlock(a):
            print "YES"
        else:
            print "NO"