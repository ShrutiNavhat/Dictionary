
# Q13.Write a Python program to sum all the items in a dictionary.


a={1:10,2:20,3:30,4:40}
sum=0
sum1=0
for i in a:
    sum=sum+a[i]
    sum1+=i
print(sum+sum1)
