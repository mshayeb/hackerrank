# Flipping Bits
# Short Problem Definition:

#You will be given a list of 32 bits unsigned integers. You are required to output the list of the unsigned integers you get by flipping bits in its binary representation (i.e. unset bits must be set, and set bits must be unset).

def flipBits(a):
   return a ^ 4294967295 # 2^32 - 1
 
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(0,n):
        a = int(raw_input())
        res = flipBits(a)
        print res