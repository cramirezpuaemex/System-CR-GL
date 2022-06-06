import matplotlib.pyplot as plt
import numpy as np
import math

x=[1.2, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.1]
y=[1,2,1,7,7,18,41,79,74,80,87,65,47,21,9,3,1]

print len(x), len(y)


N=[]
total=0
for i in y:
	total+=i

print total
for i in y:
	if total >1:
		N.append(total-i)
		total=total-i
	else:
		N.append(i)
	
print N

aux_N=[]
for i in N:
	print math.log10(i)
	aux_N.append(math.log10(i))

y=aux_N	
x_2=0
xy=0
sum_y=0
sum_x=0
xlny=0
lny=0
for i in range(len(x)-2):
	x_2+=(x[i]*x[i])
	xy+=x[i]*y[i]
	sum_y+=y[i]
	sum_x+=x[i]
	xlny=x[i]+math.log(y[i])
	lny+=math.log(y[i])
print aux_N
#a=((x_2*(sum_y))-(xy*sum_x))/((len(x)*(x_2))-((sum_x*sum_x)))
a=((len(x)*(xlny))-(sum_x*lny))/((len(x)*(x_2))-(sum_x*sum_x))
print a
#b=((len(x)*xy)-(sum_y*sum_x))/((len(x)*x_2)-((sum_x*sum_x)))
b=((x_2*lny)-(xlny*sum_x))/((len(x)*x_2)-(sum_x*sum_x))
print b


#
bb=math.exp(b)
new=[]
for i in x:
	#new.append((b*i)-a)
	new.append(bb*math.exp(a*i))




plt.plot(x,y, color='darkgreen', marker='^')
plt.plot(x,new, color='red', marker='^' )
plt.show()