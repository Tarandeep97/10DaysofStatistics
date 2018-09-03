import math
sqrt = math.sqrt
erf = math.erf
def N(x,mu1,sd1):
    ans  = 0.5 *(1+ erf((x-mu1)/(sd1*sqrt(2))))
    return ans


ans = N(9800,205*(49),15*sqrt(49))
print(round(ans,4))
