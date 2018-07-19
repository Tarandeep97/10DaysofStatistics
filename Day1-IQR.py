def quartile(arr):
    l = len(arr)
    if l%2 ==0:
        median = (arr[l//2-1]+arr[l//2])/2
    else:
        median = (arr[l//2])
        
    return(median)
def main():
    N = int(input())
    data = list(map(int,input().split()))
    freq = list(map(int,input().split()))
    X =[]
    for i in range(len(data)):
        X = X + [data[i]]*freq[i]
        
    X = sorted(X)
    n = len(X)
    L = X[:n//2]
    if n%2==0:
        U = X[n//2:]
    else:
        U = X[n//2+1:]
    Q1 = quartile(L)
    Q2 = quartile(X)
    Q3 = quartile(U)
    print('{0:0.1f}'.format(Q3-Q1))
    
    
if __name__=='__main__':
    main()
