# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.


# l="MISSISSIPPI"
# a=list(l)
# i=0
# b=[]
# while i<len(a):
#     j=0
#     b1=[]
#     count=0
#     while j<len(a):
#         if a[i] in a:
#             if a[i]==a[j]:
#                 count=count+1
#             j=j+1
#     b1.append (a[i])
#     b1.append(count)
#     if b1 not in a:
#         b.append(b1)
#     i=i+1
# print(dict(b))





x=input("enter the number : ")
if x>="a" and x<="z":
    print(x,"alphabet")
elif x>"0"<x:
    print(x,"number")
else:
    print(x,"special character")


    
