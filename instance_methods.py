
class User:

    # yapici metot (constructor)
    def __init__(self, _username, name, surname, birthday):
        # object attribute, instance attribute
        self.username = _username
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def info(self):
        return f"{self.username} kullanici adiyla {self.name} {self.surname} sisteme kaydedildi."
    def calculateAge(self):
        return f"{self.username} kullanicisin yasi {2022-self.birthday}"
u1 = User("leventert","Levent","Ertunalilar",1984)

print(u1.info())
print(u1.calculateAge())