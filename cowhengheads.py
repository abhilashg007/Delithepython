head=int(input("Enter the heads:"))
leg=int(input("Enter the legs:"))

cow=0
hen=0

for hen in range(head):
    cow=head-hen
    if(cow*4 + hen*2 == leg):
        print("COWS :",cow)
        print("HENS :",hen)
        flag=True
        break
if(not flag):
    print("No flag")
    
    
