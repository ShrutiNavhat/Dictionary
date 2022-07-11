a={'sum':{1:4,3:7,8:9}}
b=int(input("enter the key :"))
c=int(input("enter the value"))
for i,j in a.items():
    for k in j:
        if k==b:
            j[k]+=c
print(a)