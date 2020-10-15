a=np.linspace (0,10,1000)
def f(x):
    p=x+2
    Q=p**2+2*p
    return Q

fdata=[]

for i in a:
    data1=f(i)
    fdata.append(data1)

h=(4*np.pi)/20000000

ydata=[]

def y(x):
    return (f(x+h)-f(x))/h

for i in a:
    data2=y(i)
    ydata.append(data2)
import matplotlib.pyplot as plt
plt.plot(a,fdata)
plt.plot(a,ydata)

