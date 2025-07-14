#euclidean algorithm
#1.Traversal
#2.special algorithm

a=int(input("Enter the num1"))
b=int(input("Enter the num2"))
rem=0
while(b!=0):
    rem=a%b
    a=b
    b=rem
print(a)
   
