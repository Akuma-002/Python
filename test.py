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
    
    
a = {"name" : "sahil"}
