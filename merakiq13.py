
# Write a program to sort a dictionary in ascending or descending according to its values .




import operator


a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
print("orginal dictionary :",a)
sorted_a=sorted(a.items(),key=operator.itemgetter(1))
print("dictionary in ascending order by value :",sorted_a)
sorted_a=sorted(a.items(),key=operator.itemgetter(1),reverse=True)
print("dictionary in descending  order by value :",sorted_a)

