# ompare the frequency counts of the two parts.

def buildMap(s):
    the_map = {}
    for char in s:
        if char not in the_map:
            the_map[char] = 1
        else:
            the_map[char] +=1
             
    return the_map       
     
 
def anagram(s1, s2):
    map1 = buildMap(s1)
    map2 = buildMap(s2)
     
    diff_cnt = 0
    for key in map2.keys():
        if key not in map1:
            diff_cnt += map2[key]
        else:
            diff_cnt += max(0, map2[key]-map1[key])
             
    for key in map1.keys():
        if key not in map2:
            diff_cnt += map1[key]
        else:
            diff_cnt += max(0, map1[key]-map2[key])
     
    return diff_cnt
 
if __name__ == '__main__':
    s1 = raw_input()
    s2 = raw_input()
    print anagram(s1, s2)