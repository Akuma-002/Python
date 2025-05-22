first_number = int(input("enter the first number "))
operator = input("enter operator (+,-,*,/,%) : ")
last_number = int(input("enter last number "))
# result

if operator == "+":
    print(first_number + last_number)
elif operator == "-":
    print(first_number - last_number)
elif operator == "*":
    print(first_number * last_number)
elif operator == "/":
    print(first_number / last_number)
elif operator == "%":
    print((first_number / last_number) * 100)
else:
    print("invalid")