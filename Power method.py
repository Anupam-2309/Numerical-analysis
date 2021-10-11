from sympy import *
B=eval(input("Enter your dimension of matrix ...\n e.g  3X3 then enter 3*3 : "))
if B==2*2:
        print(" ")
        a=eval(input("Enter your 1st row Value with ' , '  : "))
        b=eval(input("Enter your 2nd row Value with ' , '  : "))
        print(" ")
        print("Your Matrix is...")
        A=(Matrix([[a[0],a[1]],[b[0],b[1]]]))
        pprint(A)
        print(" ")
        X=det(A)
        Zero=zeros(2,1)
        print(" ")
        d=eval(input("Enter your Coulum Value Of Initial Vector ...with ' , '  : "))
        X0=(Matrix([[d[0]],[d[1]]]))        
elif B==3*3:
        a=eval(input("Enter your 1st row Value with ' , '  : "))
        b=eval(input("Enter your 2nd row Value with ' , '  : "))
        c=eval(input("Enter your 3rd row Value with ' , '  : "))
        print(" ")
        print("Your Matrix is...")
        A=(Matrix([[a[0],a[1],a[2]],[b[0],b[1],b[2]],[c[0],c[1],c[2]]]))
        pprint(A)
        print(" ")
        X=det(A)
        Zero=zeros(3,1)
        print(" ")
        d=eval(input("Enter your Coulum Value Of Initial Vector ...with ' , '  : "))
        X0=(Matrix([[d[0]],[d[1]],[d[2]]]))
else:
    print(" ")
    print("Please enter appropriate dimension of matrix ,use ' * ' \n Only square matrix ")
    

print("Intial Vectors is  X0 =: ")
pprint(X0)
print(" ")

print("------------Iteration-0------------")
AX=A*X0
print("A*X0 = ",AX.evalf(3))

L1=max(AX)
print("λ1 =",L1.evalf(2))

X1=(AX/L1)
print("X1 =",X1.evalf(2))
print(" ")
Z=X0.evalf(2)-X1.evalf(2)

while Z!=Zero:
    for i in range(1,10):
        X0=X1
        AX=A*X0
        L1=max(AX)
        X1=(AX/L1)
        print(" ")
        print("------------Iteration-"+str(i)+"------------")
        print("A*X"+str(i)+" = " ,AX.evalf(3))
        print(" ")
        print("New Eigen Value and Eigen Vectors ...")
        print(" ")
        print("λ"+str(i+1)+" = ",L1.evalf(3))
        print("X"+str(i+1)+" = ",X1.evalf(3))
        print(" ")
        Z=X0.evalf(2)-X1.evalf(2)
else:
    print(" ")
    print("-----------------------------------------------------------")
    print("Largest Eigen value is : ",L1.evalf(3))
    print("And Eigen Vector is : ",X1.evalf(3))
