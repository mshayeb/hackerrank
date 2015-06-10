# Just follow the instructions.

def isStrFunny(s):
    s_len = len(s)
    idx = 0
    while idx < s_len//2:
        left_diff = abs(ord(s[idx]) - ord(s[idx+1]))
        right_diff = abs(ord(s[s_len-idx-1]) - ord(s[s_len-idx-2]))
        if left_diff != right_diff:
            return False
        idx += 1
     
    return True
     
 
if __name__ == '__main__':
    t = input()
    for _ in range(t):
        s = raw_input()
        if isStrFunny(s):
            print "Funny"
        else:
            print "Not Funny"
