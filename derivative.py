import numpy as np
import matplotlib.pyplot as plt
xdata=np.linspace(0,4*np.pi,1000)
def f(x):
    return np.cos(x)
fdata=[]
for i in (xdata):
    data=f(i)
    fdata.append(data)
h=4*np.pi/1000
def fprime(x):
    return (f(x+h)-f(x))/h
ydata=[]
for x in (xdata):
    Ydata=fprime(x)
    ydata.append(Ydata)
plt.plot(xdata,fdata)
plt.plot(xdata,ydata)
