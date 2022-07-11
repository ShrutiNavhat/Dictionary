# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :



# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in dic1,dic2,dic3:
#     dic4.update(i)
# print(dic4)

# def a(b,c):
#     d=b+c
#     if d>=15 and d<=20:
#         return(20)
#     else:
#         return(d)
# print(a(15,2))


def a(b=["abc","xyz","aba","chc","12321","1221"]):
    i=0
    while i<len(b):
        j=0
        count=0
        while j<len(b[i]):
            if b[i][0]==b[i][-1]:
               count=count+1
            j=j+1   
        i=i+1
    print(count)
a()


