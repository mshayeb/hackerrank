# We count the number of elements that occur in all characters  sets. Just use set intersection.

if __name__ == '__main__':
    t = input()
    all_elements = set(raw_input())
     
    for _ in xrange(t-1):
        all_elements &= set(raw_input())
         
    print len(all_elements)