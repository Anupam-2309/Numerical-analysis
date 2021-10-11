from sympy import *
A=Matrix([[-1,1,0],[1,-1,1],[0,1,-1]])
M=A**-1
X0=Matrix([[1], [1],[1]])
Zero=zeros(3,1)


print("Your Matrix is  A =: ")
a=pprint(M)
print(" ")


print("Intial Vectors is  X0 =: ")
b=pprint(X0)
print(" ")

print("------------Iteration-0------------")
AX=M*X0
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
        AX=M*X0
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
    print("Smallest Eigen value is : ",1/L1.evalf(3))
    

    
