from sympy import *
B=eval(input("Enter your dimension of matrix ...\n e.g  3X3 then enter 3*3 : "))
if B==2*2:
        print(" ")
        a=eval(input("Enter your 1st row Value with ' , '  : "))
        b=eval(input("Enter your 2nd row Value with ' , '  : "))
        print(" ")
        print("Your Matrix A is...")
        A=(Matrix([[a[0],a[1]],[b[0],b[1]]]))
        pprint(A)
        print(" ")
elif B==3*3:
        a=eval(input("Enter your 1st row Value with ' , '  : "))
        b=eval(input("Enter your 2nd row Value with ' , '  : "))
        c=eval(input("Enter your 3rd row Value with ' , '  : "))
        print(" ")
        print("Your Matrix A is...")
        A=(Matrix([[a[0],a[1],a[2]],[b[0],b[1],b[2]],[c[0],c[1],c[2]]]))
        pprint(A)
else:
    print(" ")
    print("Please enter appropriate dimension of matrix ,use ' * ' \n Only square matrix ")
    
        
#A=Matrix([[4,3],[1,2]])
#print("Your Matrix A is :")
#pprint(A)
A.LUdecomposition()
X=A.LUdecomposition()
B=X[1]*X[0]
i=int(input("No. of Iteration : "))
n=0
while n<i:
    A.LUdecomposition()
    X=A.LUdecomposition()
    B=X[1]*X[0]
    A=B
    print("------------","Iteration"+str(n)+"------------")
    print("L"+str(n)+" = ",X[0].evalf(3))
    print("U"+str(n)+" = ",X[1].evalf(3))
    
    print(" ")
    print("New matrix Of A is : ")
    print(B.evalf(3)," = "+"U"+str(n)+" *  L"+str(n))
    print(" ")
    n=n+1
else:
    if B==3*3:
        print("___________________________________________")
        print(" ")
        print("Eigen Values Are : ",B[0].evalf(2),"And",B[4].evalf(2),"And",B[8].evalf(2))
    else:
        print("___________________________________________")
        print(" ")
        print("Eigen Values Are : ",B[0].evalf(2),"And",B[3].evalf(2))
        
