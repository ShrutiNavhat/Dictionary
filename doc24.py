# Q23.Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

d={"a":50,"b":58,"c":56,"d":40,"e":100,"f":20}
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        max1=0
        for j in d:
            if d[j]>max1 and d[j]!=max:
                max1=d[j]
                max2=0
                for k in d :
                    if d[k]>max2 and d[k]!=max1 and d[k]!=max:
                        max2=d[k]
print(max,max1,max2)


