#given two integers, L and R, find the maximal values of A xor B, where A and B satisfies the following condition: L <= A<= <= B <= R

def  maxXor( l,  r):
  max_xor = 0
  for low in xrange(l ,r+1):
    for high in xrange(low, r+1):
        max_xor = max(max_xor, low ^ high)
  return max_xor  
 
if __name__ == '__main__':
    l = int(raw_input());
    r = int(raw_input());
 
    res = maxXor(l, r);
    print(res)
