# Level 1: Base product
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Level 2: Electronic product
class ElectronicProduct(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years

# Level 3: Mobile phone
class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty_years, ram, storage):
        super().__init__(name, price, warranty_years)
        self.ram = ram
        self.storage = storage

    def display_details(self):
        print(f"Phone: {self.name} | Price: ₹{self.price} | "
              f"Warranty: {self.warranty_years} yr | Specs: {self.ram}/{self.storage}")

phone = MobilePhone("Galaxy S25", 74999, 1, "12GB", "256GB")
phone.display_details()