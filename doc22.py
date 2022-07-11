# Q21.Write a Python program to print all unique values in a dictionary. 

data=[{"V":"S001"},{"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

b=[]
c={}
for i in range(len(data)):
    for j in data[i].values():
        if j not in b:
            b.append(j)
print(b)
