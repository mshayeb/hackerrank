# The first step is to create a count of all integers. Next there are choose(k,2)*2 distinct pairs for each integer count (this step similar to Handshake, but you count i,j and j,i as two distinct pairs). Count those together and you arrive at the answer.

def cnt_equals(arr):
    the_map = {}
    final_cnt = 0
    for value in arr:
        if value not in the_map:
            the_map[value] = 1
        else:
            the_map[value] += 1
 
    for value in the_map.values():
        if value != 1:
            final_cnt += (value*(value-1))
 
    return final_cnt
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        n = input()
        arr = map(int, raw_input().split())
        print cnt_equals(arr)
