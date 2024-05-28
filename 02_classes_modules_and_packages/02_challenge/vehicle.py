class Vehicle:
    def __init__(self, model, make, year, price, discount=0) -> None:
        self.model = model
        self.make = make
        self.year = year
        self.price = price
        self.discount = discount

    def set_model(self, model):
        self.model = model

    def set_make(self, make):
        self.make = make

    def set_year(self, year):
        self.year = year

    def set_price(self, price):
        self.price = price

    def set_discount(self, discount):
        self.discount = discount

    def get_model(self) -> str:
        return self.model
    
    def get_make(self) -> str:
        return self.make
    
    def get_year(self) -> str:
        return self.year
    
    def get_price(self) -> str:
        return self.price
    
    def get_discount(self) -> str:
        return self.discount
    
    def display(self):
        print(
            "--- CAR INFO ---\n"
            f"{'Model:':<10}{self.model}\n"
            f"{'Make:':<10}{self.make}\n"
            f"{'Year:':<10}{self.year}\n"
            f"{'Price:':<10}{self.price}\n"
            f"{'Discount:':<10}{self.discount}\n"
        )
