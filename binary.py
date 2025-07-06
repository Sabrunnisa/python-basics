a=input("enter a binary value:")
b=0
for i in range(0,len(a)):
    b=b+int(a[i])+(2**i)
print(b)    
    
