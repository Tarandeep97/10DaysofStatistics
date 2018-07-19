import math
N = int(input())
X = list(map(int,input().split()))
mu = sum(X)/ len(X)
numerator =0
for i in range(len(X)):
    numerator += (X[i]-mu)**2
    
variance  = numerator / len(X)
sd = math.sqrt(variance)
print('%0.1f' %sd)
