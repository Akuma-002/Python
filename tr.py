def check(st):
    count_u = 0
    count_l = 0
    for i in st:
        if(i.isupper()):
            count_u+=1
        else:
            count_l+=1
    return count_u,count_l

print(check("SahIl"))