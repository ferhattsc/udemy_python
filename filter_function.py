
yaslar = [7,15,18,27,36]

def yetiskinmi(x):
    if x<18:
        return False
    else:
        return True

sonuc = list(filter(yetiskinmi, yaslar))
sonuc = list(filter(lambda x: x>=18, yaslar))

#----------------------------------

sayilar = [2,5,9,8,12,67]

sonuc = list(filter(lambda x: x%2==1, sayilar))

#----------------------------------

isimler = ["ali","kemal","sinem","kaan","eray"]

sonuc = list(filter(lambda n: n[0]=="k", isimler))

secim = filter(lambda n: n[0]=="k", isimler)

sonuc = list(map(lambda n: n.upper(), secim))

#----------------------------------

users = [
    {"username": "levent", "posts": []},
    {"username": "l_ertunalilar", "posts": ["post1","post2"]},
    {"username": "levent_ertunalilar", "posts": ["post1"]}
]

post_olanlar = list(filter(lambda u: len(u["posts"])>0, users))
sonuc = list(map(lambda u: u["username"].upper(), post_olanlar))

sonuc = [user["username"] for user in users if len(user["posts"])>0]

print(sonuc)