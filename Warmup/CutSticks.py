# Cutting every stick will result in O(N^2) which is not required. Sorting the array requires nlogn time. Python pop() requires O(1) time and importantly it does not rearrange or reallocate the array.

# With each step, remove all elements from the list (actually a stack/queue) that have the same value and print the size of the remaining list.

def computeSticks(arr):
    arr.sort(reverse=True)
    while len(arr) > 0:
        print len(arr)
        block_cut = arr.pop()
        while len(arr) > 0 and arr[-1] <= block_cut:
            arr.pop()
 
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    computeSticks(arr)