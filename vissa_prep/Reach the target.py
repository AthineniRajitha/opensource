t=int(input())
for _ in range(t):
    x,y=map(int, input().split())
    winning_target=x+1
    runs_needed=winning_target-y
    print(runs_needed)
