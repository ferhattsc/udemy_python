
class User:
    
    active_users = 0

    
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


print(f"Aktif kullanici sayisi: {User.active_users}")

user1 = User("leventert","Levent","Ertunalilar",45)
user2 = User("ali_yilmaz","Ali","Yilmaz",45)
user3 = User("kemal_yalcin","Kemal","Yalcin",45)

print(f"Aktif kullanici sayisi: {User.active_users}")
print(user2.logout())
print(f"Aktif kullanici sayisi: {User.active_users}")
print(user3.logout())
print(f"Aktif kullanici sayisi: {User.active_users}")
