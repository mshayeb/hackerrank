# The cost for each present is either the cost of its category, or the cost of the other category + the conversion cost. Just select the minimum.

if __name__ == '__main__':
    t = input()
    for _ in xrange(t):
        b, w = map(int, raw_input().split())
        x, y, z = map(int, raw_input().split())
         
        print min(b*x, b*(y+z)) + min(w*(x+z), w*y)