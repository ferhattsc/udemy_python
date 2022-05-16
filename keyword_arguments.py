
def fullName(firstName, lastName):
    return f"Sisteme hosgeldiniz, {firstName} {lastName}"

sonuc = fullName("Levent","Ertunalilar")
sonuc = fullName(lastName="Ertunalilar",firstName="Levent")
print(sonuc)