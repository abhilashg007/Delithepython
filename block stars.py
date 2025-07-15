#Enter the numbers
#block1
#***********
#block2
#**********
#block3
#*********
block=int(input("Enter the block:"))
lines=int(input("Enter the lines:"))
stars=int(input("Enter the no. stars:"))
sum=0
print("--------------------------")
for i in range(block):
    print(f"----------(i+1)------------")
    count=0
    for j in range(lines-1):
        for j in range(stars):
            print("*",end=" ")
            count=count+1
        print()
    print(count)
    sum+=count
print(f"Total: {sum}")        
