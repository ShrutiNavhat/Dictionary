# Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
print("{:<10}{:<10}{:<10}".format("a","b","c"))
for key,value in my_dict.items():
    a,b,c=value
    print(("{:<10}{:<10}{:<10}".format(a,b,c)))
# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
