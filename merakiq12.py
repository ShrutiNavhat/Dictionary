# Write a program to create a dictionary with all numbers from 1 to 15 as the keys and their squares as the corresponding values.


n=int(input("enter the number :"))
b={}
for i in range(1,n):
    b.update({i:i**2})
    i=i+1
print(b)