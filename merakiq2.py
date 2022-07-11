# Write a program to print 'exists' if entered key already exists in the dictionary and print 'not exists' if the entered key does not exist.


dict1={"name":"Raju", "marks":56}
a=input("enter tne key : ")
if a in dict1:
    print(a,"exist")
else:
    print(a,"not exist")


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = thisdict.items() 
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.values()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change 