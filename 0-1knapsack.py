
#recursive version
for i in range(int(input())):
    n = int(input())
    W = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))

    def knapsack(wt, val, W, n):
        if n == 0 or W == 0:
            return 0
        elif wt[n-1] <= W:
            return max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
        elif wt[n-1] > W:
            return knapsack(wt, val, W, n-1)
    g = knapsack(wt, val, W, n)
    print(g)


#memoized version
for i in range(int(input())):
    n = int(input())
    W = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    t = [[-1 for i in range(W+1)] for j in range(n+1)]

    def knapsack(wt, val, W, n):
        if n == 0 or W == 0:
            return 0
        elif t[n][W] != -1:
            return t[n][W]
        elif wt[n-1] <= W:
            t[n][W]=max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1), knapsack(wt, val, W, n-1))
            return t[n][W]
        elif wt[n-1] > W:
            t[n][W] = knapsack(wt, val, W, n-1)
            return t[n][W]
    g = knapsack(wt, val, W, n)
    print(g)


#top down version
for i in range(int(input())):
    n = int(input())
    W = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    t = [[0 for i in range(W+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(W+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif wt[i-1] <= j:
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    g = t[n][W]
    print(g)

"""
# driver code
# no of test cases
2
#test case 1
3
4
1 2 3
4 5 1
#test case 2
3
3
1 2 3
4 5 6

#output 1 -> 3
#output 2 -> 0

"""

