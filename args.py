
numbers = [5,15,20,25]

# def topla(a,b):
#     return a + b

# def topla(a,b,c):
#     return a + b + c

# def topla(sayilar):
#     sonuc = 0
#     for i in sayilar:
#         sonuc += i
#     return f"Sayiarin toplami: {sonuc}"

# print(topla(numbers))

def topla(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(topla(5,10,15))
print(topla(5,10,15,20,25))