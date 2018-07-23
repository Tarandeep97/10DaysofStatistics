"""A random variable, , follows Poisson distribution with mean of 2.5. Find the probability with which the 
random variable is equal to 5.
"""

mean = float(input())
X = int(input())
e = 2.71828
import math
fact = math.factorial
ans = (((mean**X)*e**(-mean))/fact(X))
print(round(ans,3))
