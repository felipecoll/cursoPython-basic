a = [1,2,3,4,5]
b = a 

print(a)
print(b)

del a[0]
print(id(a))
print(id(b))
