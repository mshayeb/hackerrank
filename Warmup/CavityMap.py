# You only get your cavities checked on an airport. I check all 4 surrounding elements if they are strictly smaller. If so, I mark the position with an ‘X’.  Better runtime than n^2 is not possible as every element has to be visited!

def transformCavity(arr, n):
    for idx_tb in xrange(1, n-1):
        for idx_lr in xrange(1, n-1):
            if arr[idx_tb-1][idx_lr] != 'X' and int(arr[idx_tb-1][idx_lr]) < int(arr[idx_tb][idx_lr]) and \
                arr[idx_tb+1][idx_lr] != 'X' and int(arr[idx_tb+1][idx_lr]) < int(arr[idx_tb][idx_lr]) and \
                arr[idx_tb][idx_lr-1] != 'X' and int(arr[idx_tb][idx_lr-1]) < int(arr[idx_tb][idx_lr]) and \
                arr[idx_tb][idx_lr+1] != 'X' and int(arr[idx_tb][idx_lr+1]) < int(arr[idx_tb][idx_lr]):
                    arr[idx_tb][idx_lr] = 'X'
 
if __name__ == '__main__':
    n = input()
     
    arr = []
     
    for _ in xrange(n):
        line = list(raw_input())
        arr.append(line)
         
    transformCavity(arr, n)
     
    for line in arr:
        print ''.join(line)