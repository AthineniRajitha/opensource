t=int(input())
for _ in range(t):
    x,n=map(int, input().split())
    points_per_testcase=x//10
    score=n*points_per_testcase
    print(score)
