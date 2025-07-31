n = 5
for i in range(n+1):
    print("*"*i)


for i in range(n+1):
    print(" "*(n-i), "*"*i)
    
    
    

count = 1
for i in range(n):
    for j in range(i+1):
        print(count, end=" ")
        count+=1
    print("\n")