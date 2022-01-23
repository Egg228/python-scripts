

x = (9,8,7,6,5,4,3)
y =[]
for i in range(len(x)):
    y.append(x[i] +3)
print(y)

t = list(x)
t[0] =10
x = tuple(t)
print(x)

x += (4,5)
print(x)
