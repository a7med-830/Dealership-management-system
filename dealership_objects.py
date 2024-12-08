class Cars:

    cars_num = 0
    available_cars = []

    def __init__(self, brand, model, year, form, price, isAvailable):
        self.brand = brand 
        self.model = model
        self.year = year
        self.form = form
        self.price = price
        self.isAvailable = isAvailable

        Cars.cars_num += 1 
        Cars.available_cars.append(self)
        
    @staticmethod
    def add_car():
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        form = input("Enter form: ")
        price = float(input("Enter price: "))
        
        Cars(brand, model, year, form, price, True)

    def get_info(self):
        print(f"Car name: {self.brand} {self.model}")
        print(f"Year: {self.year}")
        print(f"Form: {self.form}")
        print(f"Price: ${self.price}")
        print("Available for purchase" if self.isAvailable else "Sold")
        print("-" * 30)

    @staticmethod
    def display_available_cars():
        print("Available Cars:")

        if not Cars.available_cars:
            print("No cars available.")

        for car in Cars.available_cars:
            car.get_info()

    def buy(self):
        if self.isAvailable:
            print(f"you have bought {self.brand} {self.model}")
            Cars.cars_num -= 1 
            self.isAvailable = False
            Cars.available_cars.remove(self)
        else:
            print(f"{self.brand} {self.model} is not available for purchase")


    def return_(self):
        print(f"you have returned {self.brand} {self.model}")
        Cars.cars_num += 1
        self.isAvailable == False

    @staticmethod
    def cars_number():
        if Cars.cars_num == 1:
            print(f"We have 1 car available") #يا تفاصيلك يا روكستار :)
        else:
            print(f"We have {Cars.cars_num} cars available")
            

class Customer:


    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.purchased_vehicles = []

    def add_purchase(self, car):
        if car.isAvailable:
            car.buy()
            self.purchased_vehicles.append(car)
        else:
            print(f"{car.brand} {car.model} is not available for purchase")

    def display_purchases(self):
        if self.purchased_vehicles:
            print(f"{self.name} has purchased the following vehicles:")
            for car in self.purchased_vehicles:
                print(f"- {car.brand} {car.model}")
        else:
            print(f"{self.name} has not purchased any vehicles.")

if __name__ == "__main__" :
    print("please open dealership management system.py")