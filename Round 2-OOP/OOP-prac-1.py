class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(self.brand, self.model, self.year)



c1 = Car("Ferari", "Purosangue", "2024")
c2 = Car("Lamborghini", "Urus", "2025")

c1.display_info()
c2.display_info()