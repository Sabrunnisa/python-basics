l=eval(input("enter a list of strings:"))
f=True
a=min(l ,key=len)
b=len(a)
print(a,b)
s=0
x=0
y=len(l)
while x<len(l):
    for z in range(y):
        for i in range(b):
            s=str(s)+l[z][i]
        while True:
            if a==s:
               continue
            else:
               f=False
               break
        s=0
        x=x+1
if not f:
    print("there is no common prefix")
else:
    print("The common prefix is:",a)
    
