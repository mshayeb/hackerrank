# I solve this challenge using DFS and dynamic programming. I iterate over all n positions (denoted with .) using DFS. For each node, I remember the number of crossroads Hermione encountered up to that point. DFS does not guarantee to find the optimal solution in terms of path length.

from collections import defaultdict
 
def hermionesWand(arr, K, max_x, max_y):
    # find both entry and exit points
    for idx, line in enumerate(arr):
        for inner_idx in xrange(len(line)):
            if line[inner_idx] == 'M':
                h = (idx, inner_idx)
            if line[inner_idx] == '*':
                e = (idx, inner_idx)
 
    st = [h]
    tracker = defaultdict(int)
    tracker[h] = 0
 
    # iterate the DFS list
    while st:
        curr = st.pop()
 
        # exit found
        if (curr == e):
            return tracker[curr] == K
 
        # save all exits that were not visited before
        inner_st = set()
        if (curr[0] > 0 and (arr[curr[0]-1][curr[1]] == "." or arr[curr[0]-1][curr[1]] == "*")) \
        and (curr[0]-1, curr[1]) not in tracker:
            inner_st.add((curr[0]-1, curr[1]))
        if (curr[1] > 0 and (arr[curr[0]][curr[1]-1] == "." or arr[curr[0]][curr[1]-1] == "*")) \
        and (curr[0], curr[1]-1) not in tracker:
            inner_st.add((curr[0], curr[1]-1))
        if (curr[0] < max_y -1 and (arr[curr[0]+1][curr[1]] == "." or arr[curr[0]+1][curr[1]] == "*")) \
        and (curr[0]+1, curr[1]) not in tracker:
            inner_st.add((curr[0]+1, curr[1]))
        if (curr[1] < max_x -1 and (arr[curr[0]][curr[1]+1] == "." or arr[curr[0]][curr[1]+1] == "*")) \
        and (curr[0], curr[1]+1) not in tracker:
            inner_st.add((curr[0], curr[1]+1))
 
        # a crossroad
        if len(inner_st) > 1:
            tracker[curr] += 1
 
        # save the nodes to DFS list
        for n in inner_st:
            tracker[n] = tracker[curr]
            st.append(n)
 
    return False
 
if __name__ == '__main__':
    t = int(raw_input())
    for _ in xrange(t):
        n, m = map(int, raw_input().split())
        a = []
        for line in xrange(n):
            a.append(list(raw_input()))
        k = int(raw_input())
        if hermionesWand(a, k, m, n):
            print "Impressed"
        else:
            print "Oops!"