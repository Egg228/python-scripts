# def name(z,x,*c, key):
#     print(z)
#     print(x)
#     print(c)
#     print(key)
# name(1,2,3,5,6,7, key=10)

def exclusive_item(*args, sorting=False,reversing =False ):
    list = []
    for i in args:
        for y in i:
            if y not in list:
                list.append(y)
    if sorting == True:
        list.sort()
    if reversing == True:
        list.reverse()
    return list
x = [4,5,7,8,2]
c = [1,2,3,5,6,7,3]
z = [9,8,7,6,5,4,]
t = exclusive_item(x,c,z,sorting=0,reversing=0)
print(t)