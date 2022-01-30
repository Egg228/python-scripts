z = {1,2,3,4,5}
x = {3,4,5,6,7}
c = {7,8,9,10}
z.add(6)
z.remove(6)  #
z.discard(5) # same as remove, when no element no error
y = z.union(x,c)
print(y)
t = z.intersection(x)
t = z.difference(x)
print(t)