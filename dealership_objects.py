class Vehicle:
    def __init__(self, brand, model, year, price, isAvailable):
        self.brand = brand 
        self.model = model
        self.year = year
        self.price = price
        self.isAvailable = isAvailable

    def get_info(self):
        print(f"Vehicle name: {self.brand} {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price}")
        print("Available for purchase" if self.isAvailable else "Sold")
        print("-" * 30)

    def buy(self):
        if self.isAvailable:
            print(f"You have bought {self.brand} {self.model}")
            self.isAvailable = False
        else:
            print(f"{self.brand} {self.model} is not available for purchase")

    def return_(self):
        print(f"you have returned {self.brand} {self.model}")
        Cars.cars_num += 1
        self.isAvailable = False

    @staticmethod
    def display_available_vehicles(vehicle_list, vehicle_type="Vehicles"):
        print(f"Available {vehicle_type}:")
        if not vehicle_list:
            print(f"No {vehicle_type.lower()} available.")
            return
        for vehicle in vehicle_list:
            vehicle.get_info()

class Cars(Vehicle):

    cars_num = 0
    available_cars = []

    def __init__(self, brand, model, year, form, price, isAvailable):
        super().__init__(brand, model, year, price , isAvailable)
        self.form = form
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


    @staticmethod
    def display_available_cars():
        print("Available Cars:")

        if not Cars.available_cars:
            print("No cars available.")

        for car in Cars.available_cars:
            car.get_info()


    @staticmethod
    def cars_number():
        if Cars.cars_num == 1:
            print(f"We have 1 car available") #يا تفاصيلك يا روكستار :)
        else:
            print(f"We have {Cars.cars_num} cars available")
            

class Bikes(Vehicle):

    bikes_num = 0
    available_bikes = []

    def __init__(self, brand, model, year, form, price, isAvailable):
        super().__init__(brand, model, year, price , isAvailable)
        self.form = form
        Bikes.bikes_num += 1 
        Bikes.available_bikes.append(self)
        
    @staticmethod
    def add_bike():
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        form = input("Enter form: ")
        price = float(input("Enter price: "))
        
        Bikes(brand, model, year, form, price, True)


    @staticmethod
    def display_available_bikes():
        print("Available Bikes:")

        if not Bikes.available_bikes:
            print("No bikes available.")

        for bike in Bikes.available_bikes:
            bike.get_info()

    
    @staticmethod
    def bikes_number():
        if Bikes.bikes_num == 1:
            print(f"We have 1 bike available") #يا تفاصيلك يا روكستار :)
        else:
            print(f"We have {Bikes.bikes_num} bikes available")


class Customer:


    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.purchased_vehicles = []

    def add_purchase(self, vehicle):
        if vehicle.isAvailable:
            vehicle.buy()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"{vehicle.brand} {vehicle.model} is not available for purchase")

    def display_purchases(self):
        if self.purchased_vehicles:
            print(f"{self.name} has purchased the following vehicles:")
            for vehicle in self.purchased_vehicles:
                print(f"- {vehicle.brand} {vehicle.model}")
        else:
            print(f"{self.name} has not purchased any vehicles.")

if __name__ == "__main__" :
    print("please open dealership management system.py")