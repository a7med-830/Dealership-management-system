class Cars:

    cars_num = 0

    def __init__(self, brand, model, year, form, price):
        self.brand = brand 
        self.model = model
        self.year = year
        self.form = form
        self.price = price

        Cars.cars_num += 1 

    def get_info(self):
        print(f"Car name : {self.brand} {self.model}")
        print(f"Car model : {self.model}")
        print(f"price : ${self.price}")

    def buy(self):
        print(f"you have bought {self.brand} {self.model}")
        Cars.cars_num -= 1 

    def borrow(self):
        print(f"you have borrowed {self.brand} {self.model}")
        Cars.cars_num -= 1 

    def return_(self):
        print(f"you have returned {self.brand} {self.model}")
        Cars.cars_num += 1


    def Cars_number():
        if Cars.cars_num == 1:
            print(f"We have 1 car")
        else:
            print(f"We have {Cars.cars_num} cars")
            
    