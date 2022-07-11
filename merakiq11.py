# Write a program to print the top 3 highest values of a given dictionary.

dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
for i in dict:
    if dict[i]>max:
        max=dict[i]
        max1=0
        for j in dict:
            if dict[j]>max1 and dict[j]!=max:
                max1=dict[j]
                max2=0
                for k in dict:
                    if dict[k]>max2 and dict[k]!=max1 and dict[k]!=max:
                        max2=dict[k]
print(max,max1,max2)