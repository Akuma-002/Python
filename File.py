text = open("file.txt", "a+")
tex = input("Enter: ")
text.writelines("\n"+tex)
text = open("file.txt", "r")
print(text.readlines())
text.close()