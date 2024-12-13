# dealership_objects.py
from database import *
from tabulate import tabulate
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

class Cars(Vehicle):

    cars_num = 0
    available_cars = []

    def __init__(self, brand, model, year, form, price, isAvailable):
        super().__init__(brand, model, year, price , isAvailable)
        self.form = form
        Cars.cars_num += 1 
        
        
    @staticmethod
    def add_car():
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        form = input("Enter form: ")
        price = float(input("Enter price: "))
        
        new_car = Cars(brand, model, year, form, price, True)

        add_car_to_db(new_car)

        print("Car added successfully to the database!")

    @staticmethod
    def display_available_cars():
        print("Available Cars:")

        cars_from_db = fetch_all_cars()
        if not cars_from_db:
            print("No cars available in the database.")
            return

        print(tabulate(cars_from_db, headers=["ID", "Brand", "Model", "Year", "Form", "Price", "Available"]))

        # for car in cars_from_db:
        #     print(f"ID: {car[0]} | Brand: {car[1]} | Model: {car[2]} | Year: {car[3]} | Form: {car[4]} | Price: ${car[5]} | Available: {'Yes' if car[6]=='Yes' else 'No'}")

    @staticmethod
    def cars_number():
        if Cars.cars_num == 1:
            print(f"We have 1 car available") 
        else:
            print(f"We have {Cars.cars_num} cars available")
   
    @staticmethod
    def delete_car():
        Cars.display_available_cars()
        id_num = input("Enter ID of the car you want to delete : ")
        delete_car_from_db(id_num)
        input("Press Enter to return to the menu.")
        
            

class Bikes(Vehicle):

    bikes_num = 0

    def __init__(self, brand, model, year, price, isAvailable):
        super().__init__(brand, model, year, price , isAvailable)
        Bikes.bikes_num += 1 
        
        
    @staticmethod
    def add_bike():
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        year = input("Enter year: ")
        price = float(input("Enter price: "))
        
        new_bike = Bikes(brand, model, year, price, True)

        add_bike_to_db(new_bike)

        print("Bike added successfully to the database!")

    @staticmethod
    def display_available_bikes():
        print("Available Bikes:")

        bikes_from_db = fetch_all_bikes()
        if not bikes_from_db:
            print("No bikes available in the database.")
            return

        print(tabulate(bikes_from_db, headers=["ID", "Brand", "Model", "Year", "Form", "Price", "Available"]))

        # for bike in bikes_from_db:
        #     print(f"ID: {bike[0]} | Brand: {bike[1]} | Model: {bike[2]} | Year: {bike[3]} | Form: {bike[4]} | Price: ${bike[5]} | Available: {'Yes' if bike[6]=='Yes' else 'No'}")

    
    @staticmethod
    def bikes_number():
        if Bikes.bikes_num == 1:
            print(f"We have 1 bike available") 
        else:
            print(f"We have {Bikes.bikes_num} bikes available")

    @staticmethod
    def delete_bike():
        Bikes.display_available_bikes()
        id_num = input("Enter ID of the bike you want to delete : ")
        delete_bike_from_db(id_num)
        input("Press Enter to return to the menu.")

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
    print("please open dealership_management_system.py")