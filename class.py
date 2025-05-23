class Student :
    name = ""
    age = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
sahil = Student("Sahil", 18)
print(sahil.name)
print(sahil.age)