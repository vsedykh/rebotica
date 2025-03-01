cde = []
class Dog:
    name = "dog"
    age = 5
    size = 67
    def __init__(self,name,age,size):
        self.name = name
        self.age = age
        self.size = size
    cde.append(name)
    cde.append(age)
    cde.append(size)
    for t in range(150):
        print(cde)