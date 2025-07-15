str1=input("Enter the string 1")
str2=input("Ente rhe string 2")
a=str1.lower()
b=str2.lower()
a1="".join(i for i in a if i!=" ")
b1="".join(i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("It is an anagram")
else:
    print("It is not an anagram")
