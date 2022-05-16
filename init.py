
class Product:
    def __init__(self, name, price, isActive=True):
        self.name = name
        self.price = price
        self.isActive = isActive
        print("product nesnesi olusturuldu")

p1 = Product("Mercedes A","600000")
p2 = Product("BMW 320","500000",False)
p3 = Product("Opel Astra","300000",True)

print(p1.name,p1.price,p1.isActive)
print(p2.name,p2.price,p2.isActive)
print(p3.name,p3.price,p3.isActive)