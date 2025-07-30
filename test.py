num = int(input("Enter a number: "))
flag = 0
for i in range(1, num):
    if (flag > 1 or num <=0):
        break
    if(num % i == 0):
        flag+=1
if(flag == 1):
    print("Prime")
else:
    print("Not Prime")