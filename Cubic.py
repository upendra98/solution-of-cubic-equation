import numpy as np

a = float(input("Enter a= "))
b = float(input("Enter b= "))
c = float(input("Enter c= "))
d = float(input("Enter d= "))
"""
a=input("a: ")
b=input("b: ")
c=input("c: ")
d=input("d: ")
"""
#a=2
#b=-5
#c=-6
#d=1
f=((3*c/a)-(b**2/a**2))/3
g=((2*b**3/a**3)-(9*b*c/a**2)+(27*d/a))/27
h=(g**2/4)+(f**3/27)
if h<0:
    i=np.sqrt((g**2/4)-h)
    j=i**(1/3)
    k=np.arccos(-g/(2*i))
    l=-j
    m=np.cos(k/3)
    n=np.sqrt(3)*np.sin(k/3)
    p=(-b/(3*a))
    x11=2*j*m+p
    x22=l*(m+n)+p
    x33=l*(m-n)+p
    print ("x1 : ",x11 )
    print ("x2 : ", x22)
    print ("x3 : ", x33)
else:
    r=-g/2+np.sqrt(h)
    if r<0:
        s=-(abs(r)**(1/3))
    else:
        s=(abs(r)**(1/3))
    t=-g/2-np.sqrt(h)
    if t<0:
        u=-abs(t)**(1/3)
    else:
        u=abs(t)**(1/3)
    
    x1=s+u-(b/(3*a))
    real=-((s+u)/2)-(b/(3*a))
    ima=(s-u)*(np.sqrt(3))/2
    print ("x1 :",x1)
    print ("x2 : ",real,"+i",ima)
    print ("x3 : ",real,"-i",ima)
