a=input("Enter the password:")
sp=0
dg=0
lw=0
up=0
if (len(a)>7):
  for i in a:
        if i.isdigit():
            dg+=1
        elif i.isupper():
            up+=1
        elif i.islower():
            lw+=1
        else:
            sp+=1
  if(sp>0 and dg>0 and lw>0 and up>0):
      print("Good password")
  else:
      print("Bad password")
        
