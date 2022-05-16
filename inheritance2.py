
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi olusturuldu.")

    def info(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    pass



class Teacher(Person):
    pass

p1 = Person("Esin","Senturk",20)
p1.info()

s1 = Student("Kerem","Koc",15)
s1.info()

t1 = Teacher("Cagla","Sahin",45)
print(t1.name,t1.surname,t1.age)    # uzun kullanimi