# n = 5
# for i in range(n+1):
#     print("*"*i)


# for i in range(n+1):
#     print(" "*(n-i), "*"*i)
    
    
    

# count = 1
# for i in range(n):
#     for j in range(i+1):
#         print(count, end=" ")
#         count+=1
#     print("\n")
    
    
# for i in range(n+1):
#     print(" "*(n-i),"*"*((i*2)-1))

# str = "Hello'''"
# print(str.rstrip("'"))

# a = [1, 2 , 3, 4, 5, 6, 7, "sahil"]
# d = ("sahil", 12)
# s = {
#     "name": "Sahil",
#     "age" : 18
# }
# t = 123456789033
# print(t)
# print(d)
# for i in a:
#     print(i)
    

# a.append("Ram")

# for i in a:
#     print(i)
    
    
# a = "sahil"
# for i in range(1, len(a)+1):
#     print(a[-i], end='')
    



# #Next
# na = input("Enter a word: ")
# count = 0
# for i in na:
#     if (i == "a"or i=='e' or i == 'i' or i == 'o' or i == 'u'):
#         count+=1
# print(f"Total vowals are : {count}")


# st = input("Enter a string: ")
# count = 0
# for i in range(0, int(len(st)/2)):
#     if(st[i] == st[(-(i+1))]):
#         count += 1
# if(count == int(len(st)/2)):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# st = input("Enter a string : ")
# temp = ""
# for i in range(len(st)):
#     if (st[i] == 'a'or st[i] == 'e'or st[i] == 'i'or st[i] == 'o'or st[i] == 'u'):
#         temp+="*"
#     else:
#         temp+=st[i]
# print(temp)


# st = input("Enter a string: ")
# a = []
# for i in st:
#     if ((i not in a) and i !=' '):
#         a.append(i)
#         print(f"{i} in this string is : ",st.count(i))



# a=int(input("enter a no."))
# flag = False
# if a <=1:
#     print("the no. is not a prime no.")
# elif a==2:
#     print("the no. is a prime no.")
# else:
#     for i in range(2,a):
#         if (a%i == 0):
#             flag = False
#             print("the no. is not a prime no.")
#             break
#         else:
#             flag=True
# if(flag):
#     print("Prime Number")

# num = int(input("Enter a number: "))
# flag = True
# for i in range(2, num):
#     if(num%i == 0):
#         flag = False
# if(flag):
#     print("Prime")
# else:
#     print("Not prime")


# rows = 4 
# for i in range(1, rows+1):
#     print(" "*(rows-i), " *"*i)
    
    
#a = {"name" : "sahil"}

# st = input("Enter a string : ")
# temp = ""
# templi = []
# for i in range(0, len(st)):
#     if(st[i] == " "):
#         if((temp != "") or (st[i] != ',')):
#             templi.append(temp)
#         temp=""
#     elif(i == len(st)-1):
#         temp += st[i]
#         templi.append(temp)
#     else:
#         temp += st[i]
    
# counter = []
# print(templi)
# for i in range(0, len(templi)):
#     counter.append(0)
#     for j in range(0, len(templi)):
#         if (templi[i] == templi[j]):
            
#             counter[i] += 1
# f = counter.index((max(counter)))
# print(f"{templi[f]} is - {max(counter)}")

# st = input("Enter a string : ")
# for i in range(0, len(st)):
#     print(st)
#     st = st.replace(st[len(st)-1-i], ' ')

# gcd 

# n1 = int(input("Enter First number: "))
# n2 = int (input("Enter Last number: "))
# out = 1
# for i in range(2, min(n1, n2)+1):
#     if((n1 % i == 0) and (n2 % i==0)):
#         out = i
# print(out)

# lis = [1, 2, 3, 2, 4, 3, 5, 2, 4, 5, 6, 2, 2, 2, 2]
# out = []
# for i in lis:
#     if i not in out:
#         out.append(i)
# print(out)


# flowers = ["Blue-Spider Lili", "Sakura", "Lavender"]
# flowers.append("Marigold")
# flowers.insert(2, "Rose")
# flowers.pop(4)
# flowers.sort(reverse=True)
# print(f"Count of Rose is {flowers.count("Rose")}")
# print(flowers[2].upper())
# print(flowers)


# lis = [1, 2, 2, 3, 3, 3, 4, 5, 4, 6, 2, 7, 2]
# nLis = []

# for i in lis:
#     if i not in nLis:
#         nLis.append(i)
# lis = nLis
# print(lis)

# lis = [1, 2, 3, 4, 5, 6 , 7]
# print("Max - ", max(lis))
# print("Min - ", min(lis))
# print("Average - ", (sum(lis)/len(lis)))
# print("Sum - ", sum(lis))
# lis.reverse()
# print(lis)
# lis2 = []
# for i in lis:
#     lis2.append(i*i)
# print(lis2)
# even_sum = 0
# for i in lis :
#     if i % 2 ==0 :
#         even_sum+=i
# print(even_sum)

# lis = [1, 2, 3, 4, 5, 6, 7]
# lis.sort(reverse=True)
# print(lis[1])

# lis = []
# for i in range(21):
#     lis.append(i*i)
# print(lis)

lis = ["pasta", "pizza", "ice-cream", "pasta", "ice-cream"]
price = {
    "pasta" : 150,
    "pizza" : 250,
    "ice-cream" : 300
}
print(f"Count of pasta - {lis.count("pasta")}")
lis2 = []
for i in lis:
    if i not in lis2:
        lis2.append(i)
lis = lis2
lis.sort()
temp = 0
item = ""
for i in lis:
    if temp < price[i]:
        temp = price[i]
        item = i
print(f"{item} price is {temp}")