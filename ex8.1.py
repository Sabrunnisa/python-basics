l=eval(input("enter a list of strings to find common prefix:"))
a=min(l,key=len)
f=True
b,c=len(a),len(l)
for i in range(c):
    s=l[i][:b]
    if s==a:
        continue
    else:
        f=False
        break
if not f:
    print("there is no common prefix")
else:
    print("the common prefix is ",a)
    
    
