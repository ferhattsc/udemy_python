
sayilar = [2,67,24,47,88,11,8]

# sayilar.sort()

sonuc = sorted(sayilar)
sonuc = sorted(sayilar, reverse=True)
sonuc = sorted((2,67,24,47,88,11,8))

users = [
    {"username":"leventert","posts":["post1","post2"],"email":"abc@gmail.com"},
    {"username":"l_ertunalilar","posts":[],"email":"abc@gmail.com"},
    {"username":"levent_ertunalilar","posts":["post1"],"password":"","phone":"1234567890"}
]

sonuc = sorted(users, key=len)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda user: len(user["posts"]))

print(sonuc)
# print(sayilar)

