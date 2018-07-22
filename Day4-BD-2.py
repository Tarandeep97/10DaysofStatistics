'''
  A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected 
  because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

  No more than 2 rejects?
  At least 2 rejects?
'''
P,n = map(int,input().split())
p = P/100
import math
fact = math.factorial
def comb(n,x):
    return(fact(n))/(fact(x)*(fact(n-x)))
          
def bino(x,n,p):
           return(comb(n,x)*(p**x)*((1-p)**(n-x)))
                
ans1=0

for i in range(3):
    ans1 += bino(i,n,p)
                  
print(round(ans1,3))
ans2 = 1-(ans1-bino(2,n,p))
print(round(ans2,3))
