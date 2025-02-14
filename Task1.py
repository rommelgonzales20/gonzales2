class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car: {self.year} {self.brand} {self.model}")


car1 = Car("Lamborghini", "GT-R", 1998)
car2 = Car("Misubishi", "Civic", 2022)


car1.display_info()
car2.display_info()
