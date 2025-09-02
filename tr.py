def com(lis1, lis2):
    for i in lis1:
        if i in lis2:
            return True
    return False

print(com([1, 2, 3], [2, 5, 6]))