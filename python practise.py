a=eval(input("enter list of strings:"))
a=a.sort()
print(a)
g=[]
c=0
for i in a:
    for j in a:
        if a[i]==a[j]:
            c+=1
        else:
            continue
    g.append(c)
    c=0
a=set(a)
print(a)
a=list(a)
print(a)
greatest=g[0]
i=0
j=i+1
while i<len(g):
    if g[i]<g[j]:
        z=a[i]
        greatest=g[j]
        i+=1
        j=i+1
    else:
        i+=1
        j=i+1
        continue
print("the number that occurs many times is: " ,z)
print("number of times it occurs: ",greatest)
    
         
            
