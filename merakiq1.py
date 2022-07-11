# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.

dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
for i in dic2:
    if i in dic1:
        dic1[i]=dic1[i]+dic1[i]
        dic1.update(dic3)
    else:
        dic1[i]=dic2[i]
print(dic1)




# a=["shruti","dhanu",2,3,4,5,6]
# i=0
# sum=0
# b=[]
# c=[]
# d=[]
# e=[]
# while i<len(a):
#     if a[i]==a[0]:
#         c.append(a[i])
#     if type(a[i])==int:
#         sum=sum+a[i]
#     if a[i]==a[1]:
#         d.append(a[i])
#     i=i+1
# b.append(sum)
# e.append(c)
# e.append(b)
# e.append(d)
# print(e)