# If two following characters are the same, you have to delete one of them. A sequence of x equal characters will require (x-1) deletions.

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        s = raw_input()
        delete_cnt = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                delete_cnt +=1
        print delete_cnt