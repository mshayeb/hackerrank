#The Utopian Tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter.  Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

def printUtopianTree(cycles):
    heights = [1]
 
    for cycle_nr in xrange(1,max(cycles)+1):
        if cycle_nr % 2 == 1:
            heights.append(heights[-1]*2)
        else:
            heights.append(heights[-1]+1)
 
    for cycle in cycles:
        print heights[cycle]
 
if __name__ == '__main__':
    n = int(raw_input())
 
    cycles = []
 
    for i in range(0,n):
        cycles.append(int(raw_input()))
 
    printUtopianTree(cycles)