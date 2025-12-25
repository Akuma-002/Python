lis = [5, 4, 3, 2, 1]

# for i in range(len(lis)-1):
#     flag = True
#     for j in range(len(lis)-1-i):
#         if (lis[j+1] < lis[j]):
#             temp = lis[j+1]
#             lis[j+1] = lis[j]
#             lis[j] = temp
#             flag = False
#     if flag == True :
#         break
# print(lis)

for i in range(len(lis)-1):
    min_num = lis[i]
    idx = i
    for j in range(i, len(lis)):
        if (lis[j] < min_num):
            min_num = lis[j]
            idx = j
    temp = lis[idx]
    lis[idx] = lis[i]
    lis[i] = temp
print(lis)

# for i in range(1, len(lis)):
#     key = lis[i]
#     j = i-1
    
#     while j>=0 and key < lis[j]:
#         lis[j + 1] = lis[j]
#         j -= 1
#     lis[j + 1] = key
    
# print(lis)

