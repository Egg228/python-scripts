
x = "sdsamkmsdkvfjvnbr"
y = input("vvedite stroku\n")

for i in x:
    count = 0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
        print("Bukv ", i, "bilo", count)





