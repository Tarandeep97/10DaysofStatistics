b,g = list(map(float,input().split()))
p = b/(b+g)
import math
fact = math.factorial
def comb(n1,x1):
    return(fact(n1)/((fact(x1)*fact(n1-x1))))
    
    
def bino_d(x,n,p):
    return(comb(n,x)*(p**x)*((1-p)**(n-x)))
ans = 0 
for i in range(3,7):
    ans += bino_d(i,6,p)
    
print(round(ans,3))
    
