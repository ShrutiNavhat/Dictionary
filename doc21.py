# Write a Python program to combine two dictionary adding values for common keys.][p] 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
i=0
b={}
for i in d2:
    if i in d1:
        d1[i]+=d2[i]
        b.update(d1)
    else:
        d1[i]=d2[i]
        b.update(d2)
print(b)

# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
