import numpy as np
a=2	#float(input('Enter a: '))
b=-5	#float(input('Enter b: '))
c=7	#float(input('Enter c: '))
d1=-(b/(2*a))

d=b**2-4*a*c
d2=np.sqrt(abs(d))
if d<0:
    print('x1=',d1,"+ i.",d2/(2*a))
    print('x1=',d1,"+ i.",d2/(2*a))
else:
    print('x1=',d1+d2/(2*a))
    print('x2=',d1-d2/(2*a))
 


ANOTHER METHOD


   
import cmath  
a = 2  #float(input('Enter a: '))  
b = -5 #float(input('Enter b: '))  
c = 7  #float(input('Enter c: '))   
d = (b**2) - (4*a*c)   
x1 = (-b+cmath.sqrt(d))/(2*a)  
x2 = (-b-cmath.sqrt(d))/(2*a)  
print('x1 =',x1)
print('x2 =',x2)
    
