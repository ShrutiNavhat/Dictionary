# Q10.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. 


# b={}
# for i in range(1,16):
#     b.update({i:i**2})
# print(b)


# a=int(input("enter the number :"))
# b={}                                                            
# for i in range(1,a):
#     b.update({i:i**2})
# print(b)       

a={1:30,2:40,3:50,4:60}
# a={1:{1:30,2:40,3:50,4:60}}
b={}
sum=0
sum1=0
for i in a:
    # b.update(a[i])
    sum=sum+i
    sum1+a[i]
    b.update({sum})
    b.update({sum1})
print(b)
# sum=0
# sum1=0
# for j in b:
#     sum=sum+j
#     sum1+=b[j]
# print("sum of dict =",sum+sum1)
