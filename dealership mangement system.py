from dealership_objects import *
import os
import time

def main_menu():
    print("Welcome to the Dealership Management System!")
    print("1. Add a new car")
    print("2. Display available cars")
    print("3. Buy a car")
    print("4. Display customer purchases")
    print("5. Exit")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    customers = {}
    running = True  
    
    while running:
        clear_screen()  
        main_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            clear_screen()
            Cars.add_car()
            print("Car added successfully!")
            input("Press Enter to return to the menu.")
        
        elif choice == "2":
            clear_screen()
            Cars.display_available_cars()
            input("Press Enter to return to the menu.")
        
        elif choice == "3":
            clear_screen()
            print("Buy a car")
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")

            if name not in customers:
                customers[name] = Customer(name, phone)
            
            customer = customers[name]
            Cars.display_available_cars()
            
            try:
                car_index = int(input("Enter the number of the car to buy : ")) - 1
                car_to_buy = Cars.available_cars[car_index]
                customer.add_purchase(car_to_buy)
                input("Press Enter to return to the menu.")
            except (ValueError, IndexError):
                print("Invalid car selection!")
                input("Press Enter to return to the menu.")
        
        elif choice == "4":
            clear_screen()
            name = input("Enter customer name: ")
            if name in customers:
                customers[name].display_purchases()
            else:
                print("Customer not found!")
            input("Press Enter to return to the menu.")
        
        elif choice == "5":
            running = False
        
        else:
            print("Invalid option! Please try again.")
            input("Press Enter to continue.")
    
    # Exit message
    clear_screen()
    print("Thank you for using the Dealership Management System!")
    print("Made By Ahmed EL-Shekih")
    print("GitHub: @a7med-830")
    print("Exiting in 5 seconds", end="")
    for point in ".....":
        print(point, end="", flush=True)
        time.sleep(1)

if __name__ == "__main__":
    main()
