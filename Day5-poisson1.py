"""The manager of a industrial plant is planning to buy a machine of either type A or type B . For each day’s operation:

    >The number of repairs, X , that machine needs is a Poisson random variable with mean 0.88. The daily cost of operating X is
    C = 160 + 40X^2
    >The number of repairs, Y, that machine needs is a Poisson random variable with mean . The daily cost of operating Y is
    C = 128 + 40Y^2

Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate 
like new at the start of each day. Find and print the expected daily cost for each machine.
"""



m1 = raw_input()
l = [float(i) for i in m1.split()]


def expect2(mean):return(mean + mean**2)

x_square = expect2(l[0])
y_square = expect2(l[1])

cost_a = 160 + 40*(x_square)
cost_b = 128 + 40*(y_square)
print(round(cost_a,3))
print(round(cost_b,3))
