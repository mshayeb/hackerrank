# Compare the frequency counts of the two parts

def buildMap(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] +=1
             
    return the_map       
     
 
def anagram(s):
    if len(s)%2 == 1:
        return -1
         
    mid = len(s)//2
    s1 = s[:mid]
    s2 = s[mid:]
     
    map1 = buildMap(s1)
    map2 = buildMap(s2)
     
    diff_cnt = 0
    for key in map2.keys():
        if key not in map1:
            diff_cnt += map2[key]
        else:
            diff_cnt += max(0, map2[key]-map1[key])
     
    return diff_cnt
 
if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        s = raw_input()
        print anagram(s)