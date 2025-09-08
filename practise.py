with open ("dunki.txt", "r") as f:
    print(f.read())


class employee:
    salary = int(input("Write your salary: "))
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def returnSalary(self):
        return self.salary    

ahnuf = employee("Ahnuf" , "20")
print(ahnuf.name)
print(ahnuf.age)
print(ahnuf.returnSalary())

hala = employee("Nala thulla", "17")
print(hala.name)
print(hala.age)
print(hala.returnSalary())