#To find the sum of digits

a = int(input("Enter the Digits"))
sum=0
while(a>0):
    sum+=a%10
    a=a//10
print("sum of digits:",sum)
