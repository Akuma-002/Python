num = int(input("Enter a number: "))
res = num
for i in range(1, num):
    res*= i

print(res)