
class User:
    
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"{cls.active_users} tane kullanici var"

    @classmethod
    def from_string(cls, data_str):
        username,name,surname,age = data_str.split(",")
        return cls(username,name,surname,age)

    
    def __init__(self,username,name,surname,age):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        User.active_users += 1
    
    def userName(self):
        return f"{self.username}"

    def logout(self):
        User.active_users -= 1
        return f"{self.username} programdan cikis yapti"


print(User.display_active_users())

# user1 = User("leventert","Levent","Ertunalilar",45)
# user2 = User("ali_yilmaz","Ali","Yilmaz",45)
# user3 = User("kemal_yalcin","Kemal","Yalcin",45)
# user4 = User("kemal_yalcin","Kemal","Yalcin",45)

user5 = User.from_string("eray_sonmez,Eray,Sonmez,24")

print(User.display_active_users())
print(user5.username)
print(user5.name)
print(user5.surname)