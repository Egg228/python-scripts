#append
#insert
#sort
#reverse
#remove
#clear
#pop
#copy
#exetend
m = []
k = list(range(1,21))
b = k.copy()
for i in k:
    if i % 2 == 0:
        m.append(i)
        k.remove(i)
else:
    print(m)
    print(k)
    print(b)