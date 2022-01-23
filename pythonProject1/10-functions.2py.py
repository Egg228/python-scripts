def count_list(q,par2 =True, count = 0):
    if par2 ==True:
        typ =type(q[0])
        for i in q:
            count += 1
        return count,typ
    else:
        for i in q:
            count += 1
        return count
j = [5, 8, 9 ,4, 7]

print(count_list(j, False))


