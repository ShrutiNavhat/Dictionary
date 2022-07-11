# Q11.Write a Python script to merge two Python dictionaries

a={1:10,2:20,3:30,4:40}
b={2:30,4:30,5:10} 
c={}
for i in a,b:
    c.update(i)
print(c)

# a={1:10,2:20,3:30,4:40}



# count=0
# for i in a:
#     x=a.keys()
#     count=count+1
# print(x)
# print(count)


# a={1:10,2:20,3:30,4:40}
# count=0
# for i in a:
#     x=a.values()
#     count+=1
# print(x)
# print(count)



# name=["shruti","srushti","aarti"]
# surname=["navhat","kumbharkar","biradar"]
# b={}
# for i in range(len(name)):
#     b.update({"name":name[i],"surname":surname[i]})
#     print(b)
    

# name=["shruti","srushti","aarti"]
# age=["17","19","20"]
# b={}
# for i in range(len(name)):
#     b.update({"name":name[i],"age":age[i]})
#     print(b)


# name=input("enter the name :")
# surname=input("enter the surname :")
# age=int(input("enter the age :"))
# b={}
# for i in range(len(name)):
#     b.update({"name":name,"surname":surname,"age":age})
# print(b)





# a=int(input("enter the number :"))
# i=0
# b=[]
# while i<=a:
#     b.append(i)
#     i+=1
# j=1
# d={}
# while j<len(b):
#     if b[j]%2==0:
#         d.update({b[j]:"true"})
#     else:
#         d.update({b[j]:"false"})
#     j+=1
# print(d)
    
    