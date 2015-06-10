if __name__ == '__main__':
    t = input()
    for _ in range(t):
        s = map(int, raw_input().split())
        reductions = 0
        for i in range(0,len(s)//2):
            reductions += abs(ord(s[i]) - ord(s[-1-i]))
        print reductions 