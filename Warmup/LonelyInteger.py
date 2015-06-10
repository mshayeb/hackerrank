# Short Problem Definition: (Lonely Integer)
# There are N integers in an array A. All but one integer occur in pairs. Your task is to find out the number that occurs only once.
# Link: https://www.hackerrank.com/challenges/lonely-integer

# Complexity:
# time complexity is O(N);

# space complexity is O(1)
# Execution:
# XORing two equal numbers cancels them out. XOR all numbers together.

def lonelyinteger(a):
    answer = 0
    for candidate in a:
        answer ^= candidate
    return answer
if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)