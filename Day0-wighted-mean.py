N = int(input())
X = list(map(int,input().split()))
W = list(map(int,input().split()))
sum_XW = sum([a*b for a,b in zip(X,W)])
sum_W = sum(W)
Weighted_mean = sum_XW / sum_W
#print(Weighted_mean)
print(round(Weighted_mean,1))
