# There are 26 letters in the English alphabet. A sentence is a pangram, if it contains all 26 characters.
def getCharCnt(s):
    return len(set(c.lower() for c in s if c != ' '))
 
if __name__ == '__main__':
    s = raw_input()
    if getCharCnt(s) == 26:
        print "pangram"
    else:
        print "not pangram"
        