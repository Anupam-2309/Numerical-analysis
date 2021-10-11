#import sympy as s
from sympy import *
x=symbols('x')

#f=x**2-4*x-7.
f=eval(input("Enter your equation : "))
print(" ")
print("YOUR EQUATION : ")
pprint(f)


Df=diff(f,x)
print(" ")
print("DERIVATIVE OF YOUR FUNCTION : ")
pprint(Df)

DDf=diff(f,x,2)
print(" ")
print("DOUBLE DERIVATIVE OF YOUR FUNCTION : ")
pprint(DDf)


Formula=x-(f/Df)-(((f**2)/2)*(DDf/Df**3))
print(" ")

X=eval(input("Enter your intial x0 value : "))
print(" ")

X1=Formula.subs({x:X})

error=abs(round(X1,10)-round(X,10)) #calculating error

while error>0.001:
    for i in range(0,20):
        X1=X
        X=Formula.subs({x:X1})
        F=f.subs({x:X1})
        DF=Df.subs({x:X1})
        DDF=DDf.subs({x:X1})
        print("----------Iteration",i,"----------")
        print(" ")
        print("F(x"+str(i),")=",round(F,10))
        print("F'(x"+str(i),")=",round(DF,10))
        print("x"+str(i+1),"=",round(X,10))
        error=abs(round(X1,10)-round(X,10))
        print("error =",error)
        print(" ")
        
