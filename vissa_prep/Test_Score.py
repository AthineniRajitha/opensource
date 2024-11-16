def achieve_score(N,X,Y):
    if 0<=Y<=N*X and Y%X==0:
        print("YES")
    else:
        print("NO")
N,X,Y=map(int, input().split())
achieve_score(N,X,Y)
