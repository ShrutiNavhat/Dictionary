# a={"1":"shruti","2":23}
# for i in a:
#     x=a.keys()
# print(x)
# for i in a:
#     y=a.values()
# print(y)


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}
for i in dic1,dic2,dic3:
    dic4.update(dic1[i])
print(dic4)



# a={"name":"shruti","age":17}
# b={}
# c={}
# for i in a:
#     print(i,"keys")
#     print(a[i],"values")

