
class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("person nesnesi olusturuldu.")

    def info(self):
        print(self.name,self.surname,self.age)

class Student(Person):
    def __init__(self, name, surname, age, number):
        Person.__init__(self, name, surname, age)
        self.number = number
        print("student nesnesi olusturuldu.")

    def ortalama_al(self):
        print(f"{self.number} numarali ogrencinin ortalamasi alindi")
        



class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        Person.__init__(self, name, surname, age)
        self.brach = branch
        print("teacher nesnesi olusturuldu.")
    
    def teach(self):
        print(f"{self.name} {self.surname} isimli ogretmen {self.brach} egitimi veriyor.")

p1 = Person("Esin","Senturk",20)
p1.info()

s1 = Student("Kerem","Koc",15,200)
s1.info()
s1.ortalama_al()
t1 = Teacher("Cagla","Sahin",45,"Bilisim Teknolojileri")
t1.info()
t1.teach()
