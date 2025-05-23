import random
while True:
    print('''
    1) for snake
    2) for water 
    3) for gun 
    4) Exit
    ''')
    op = int(input("Enter your option: "))


    n = random.randint(1, 3)
    if (n == op) :
        print("Draw")
    elif(op == 4):
        break
    elif ((n == 1 and op == 2)or(n == 3 and op == 1) or (n == 2 and op == 3)):
        print("You lost, try again")
    elif ((op == 1 and n == 2)or(op == 3 and n == 1) or (op == 2 and n == 3)):
        print("You won!!!!!!")
    else:
        print("Error")
        
    if n==1 :
        print("snake")
    elif(n == 2):
        print("Water")
    elif(n == 3):
        print("Gun")