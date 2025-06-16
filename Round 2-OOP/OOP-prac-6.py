class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__tax_rate = 0.15
    def final_price(self):
        return self.price + (self.price * self.__tax_rate)
        
p1 = Product("Laptop", 1000)
p2 = Product("Smartphone", 800)

print(p1.final_price())
print(p2.final_price())
