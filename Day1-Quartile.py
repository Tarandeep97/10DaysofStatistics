def quartile(arr):
    l = len(arr)
    if l%2 ==0:
        median = (arr[l//2-1]+arr[l//2])/2
    else:
        median = (arr[l//2])
        
    return(median)
 
def main():
    N = int(input())
    X = list(map(int,input().split()))
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
    print(round(Q1))
    print(round(Q2))
    print(round(Q3))
    
if __name__=='__main__':
    main()
