# Count the total number of items from the values of the dictionary which are in the form of a list.
dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for i in dict1:
    for j in range (len(dict1[i])):
        count=count+1
print("total count : ",count)