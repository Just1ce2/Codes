from math import sqrt
x = [-1]
y = [sqrt(1-x[-1]**2)]

while x[-1] < 1:
    x.append(round(x[-1]+0.1,2))
    y.append(sqrt(1-x[-1]**2))

dist = []
for i in range(1,len(x)):
    dist.append(sqrt((x[i]-x[i-1])**2+(y[i]-y[i-1])**2))

sum(dist)