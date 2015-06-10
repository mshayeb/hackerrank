if __name__ == '__main__':
    string = raw_input()
    found = True
    # Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
    oddCnt = 0
    letterCnt = [0] * 26
     
    for letter in string:
        letterCnt[ord(letter)-ord('a')] += 1
     
    for cnt in letterCnt:
        oddCnt += cnt % 2
         
    if oddCnt > 1:
        found = False
 
    if not found:
        print("NO")
    else:
        print("YES")