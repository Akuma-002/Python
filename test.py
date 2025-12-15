def cal_op(a,b,operation):
    match operation:
        case"+":
            return a+b
        case"-":
            return a-b
        case"*":
            return a*b
        case"/":
            if b!=0:
                return a/b
            else:
                return"error"
            
no1= float(input("enter first no.:"))
no2= float(input("enter second no.:"))
operator = input("enter operator(+,-,*,/):")
result = cal_op(no1,no2,operator)
print("Result:",result)