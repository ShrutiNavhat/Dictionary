# Q27.Write a Python program to count the values associated with key in a dictionary.
# student=[{'id': 1, 'success': True, 'name': 'Lary'},{'id': 2, 'success': False, 'name': 'Rabi'},{'id': 3, 'success': True, 'name': 'Alex'}]
# x=studenyt'()'
# print(x)

# .Write a Python program to remove spaces from dictionary keys.
# Original_dictionary={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# New_dictionary= {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
# a={"s 001":["math","science"],"s 002":["math","english"]}
# b=""
# for i in a:
#     if a[i] in b:

# Write a Python program to get the top three items in a shop. Go to the editor
data={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
max=0
for i in data:
    if data[i]>max:
        max=data[i]
        a=i
        max1=0
        for j in data:
            if data[j]>max1 and data[j]!=max:
                max1=data[j]
                b=j
                max2=0
                for k in data:
                    if data[k]>max2 and data[k]!=max1 and data[k]!=max:
                        max2=data[k]
                        c=k
print(a,max,b,max1,c,max2)

# item4 55
# item1 45.5
# item3 41.3

