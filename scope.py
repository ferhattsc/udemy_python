
# global scope
# a = "global deger"

# def fn1():
#     local scope
#     a = "local deger"
#     print(a)

# fn1()
# print(a)

#-----------------------------

# city = "Istanbul"

# def changeCity(new_city):
#     city = new_city

#     print(city)

# changeCity("Bursa")
# print(city)

#-----------------------------

# city = "Istanbul"

# def dis_fonksiyon():
#     city = "Izmir"

#     def ic_fonksiyon():
#         city = "Ankara"
#         print("ic fonksiyon " + city)
    
#     ic_fonksiyon()
#     print(city)

# dis_fonksiyon()
# print(city)

#-----------------------------

a = 10

def fn2():
    
    global a

    print(f"a : {a}")

    a = 20
    print(f"changed a to {a}")

fn2()
print(a)