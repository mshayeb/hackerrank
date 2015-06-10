# You do not need to create all the arrays. Just work with an offset and array slices.

from math import sqrt, floor, ceil
 
if __name__ == '__main__':
    s = raw_input().replace(" ", "")
    columns = int(ceil(sqrt(len(s))))
    for c in xrange(columns):
        print s[c::columns],