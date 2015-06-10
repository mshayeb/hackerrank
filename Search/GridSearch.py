# There are many sophisticated 2d pattern matching algorithms out there. Just think of computer vision, robotics, gaming… The issue with most of them is, that they are rather heuristics than complete matches. I first started solving this challenge by using brute force and well.. It passed the time constraints. I did not expect that. If anyone has a good way of reducing the number of subarray checks, please post it in the comments!

# SubArray-Check reduction techniques:
#    keep the sum of the sub-array in a separate grid, check only if sum matches the pattern
#    Rabin-Karp string searching algorithm on each line to fast forward

def matchSubArray(arr, pat, x, y, pat_y, pat_x):
    for running_y in xrange(pat_y):
        for running_x in xrange(pat_x):
            if arr[running_y+y][running_x+x] != pat[running_y][running_x]:
                return False
     
    return True
             
             
def solveBruteForce(arr, pat, arr_y, arr_x, pat_y, pat_x):
    for y in xrange(arr_y-pat_y+1):
        for x in xrange(arr_x-pat_x+1):
            if matchSubArray(arr, pat, x, y, pat_y, pat_x):
                return True
     
    return False
     
if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        arr_y, arr_x = map(int, raw_input().split())
        arr = [0] * arr_y
        for y in xrange(arr_y):
            arr[y] = list(raw_input())
         
        pat_y, pat_x = map(int, raw_input().split())
        pat = [0] * pat_y
        for y in xrange(pat_y):
            pat[y] = list(raw_input())
         
        if solveBruteForce(arr, pat, arr_y, arr_x, pat_y, pat_x):
            print "YES"
        else:
            print "NO"
        