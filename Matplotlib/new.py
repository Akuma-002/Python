a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

if(a == b):
    print("Both are equal")
elif(a < b):
    print(f"{a} is smaller then {b}")
elif(a > b):
    print(f"{b} is smaller then {a}")
else:
    print("Invalid")