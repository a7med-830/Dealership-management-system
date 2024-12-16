# dealership_management_system.py
import os
import time
from pyfiglet import figlet_format
from termcolor import colored
from dealership_objects import *
from database import * 

def main_menu():
    for char in "Welcome to the Dealership Management System!":
        print(colored(char, attrs=['bold']), end="", flush=True)
        time.sleep(0.03)
    print("\n1. Display available vehicles")
    print("2. Buy a vehicle")
    print("3. Display customer purchases")
    print("4. Login as Manger")
    print("q. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1": # display vehicles
        clear_screen()
        show_choice = input("View [1] Cars🚗\n[2] Bikes🏍️? : ").strip()
        if show_choice == "1":
            Cars.display_available_cars()
        elif show_choice == "2":
            Bikes.display_available_bikes()
        else:
            print("Invalid choice!")
        input("Press Enter to return to the menu.")
        return True
    
    elif choice == "2": # buy vehicle
        clear_screen()
        print("[1] Buy Car🚗\n[2] Buy Bike🏍️")
        buy_choice = input("Choose an option: ").strip()

        if buy_choice in ["1", "2"]:
            name = input("Enter your name: ").strip()
            phone = input("Enter your phone number: ").strip()
            customer = Customer(name, phone)
            vehicle_type = "Car" if buy_choice == "1" else "Bike"

            if vehicle_type == "Car":
                Cars.display_available_cars()
            elif vehicle_type == "Bike":
                Bikes.display_available_bikes() 
            else:
                print("How did you get here ????")

            vehicle_id = int(input(f"Enter the ID of the {vehicle_type} you want to buy: ").strip())

            customer.add_purchase(vehicle_id, vehicle_type)
        else:
            print("Invalid option!")
        input("Press Enter to return to the menu.")
        return True
    
    elif choice == "3": # display purchases
        clear_screen()
        name = input("Enter your name: ").strip()
        phone = input("Enter your phone number: ").strip()
        
        customer = Customer(name, phone)
        customer.display_purchases()
        input("Press Enter to return to the menu.")
        return True
    
    elif choice == "4": # manger menu
        manger_menu()
        return True

    elif choice == "q": # quit
        return False
    
    else:
        print("Invalid option! Please try again.")
        input("Press Enter to continue.")
        return True

def manger_menu():
    access = login_as_manger()
    while True:
        if access:
            clear_screen()
            print(figlet_format("Manger Menu"))
            print("1. Display Available Vehicles")
            print("2. Add a New Vehicle")
            print("3. Delete Vehicle")
            print("4. Drop Table")
            print("5. Drop Database")
            print("6. Get Back To Main Menu")
            choice = input("Choose an option: ").strip()
        else:
            print("invalid password!")
            input("Press ENTER to get back to main menu")
            return


        if choice == "1": # display vehicles
            clear_screen()
            show_choice = input("View [1] Cars or [2] Bikes? : ").strip()
            if show_choice == "1":
                Cars.display_available_cars()
            elif show_choice == "2":
                Bikes.display_available_bikes()
            else:
                print("Invalid choice!")
            input("Press Enter to return to the menu.")

        elif choice == "2": # add vehicle
            clear_screen()
            addChoice = input("[1] Car🚗 \n[2] Bike🏍️ \nWhat do you want to add : ")
            if addChoice == "1":
                Cars.add_car()
            elif addChoice == "2":
                Bikes.add_bike()
            else:
                print("Invalid choice!")
            input("Press Enter to return to the menu.")
        
        elif choice == "3": # delete vehicle
            clear_screen()
            delChoice = input("[1] Car🚗\n[2] Bike🏍️\nWhat do you want to delete: ").strip()
            if delChoice == "1":
                Cars.delete_car()
            elif delChoice == "2":
                Bikes.delete_bike()
            else:
                print("Invalid choice!")
            input("Press Enter to return to the menu.")

        elif choice == "4":
            drop_table()
            input("Press Enter to return to the menu.")
            
        elif choice == "5":
            drop_db()
            input("Press Enter to return to the menu.")

        elif choice == "6":
            return
        
        else:
            print("Invalid choice!")
            input("Press Enter to return to the menu.")
        

def login_as_manger():
    clear_screen()
    print(figlet_format("Manger Menu"))
    password = input("Enter manger password : ").strip()
    
    if password == '123123':
        return True
    else:
        return False
    

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    running = True
    while running:
        clear_screen()  
        running = main_menu()

            
def exit_message():
        clear_screen()
        print("Thank you for using the Dealership Management System!")
        print("Made By Ahmed EL-Shekih")
        print("GitHub: @a7med-830")
        print("Exiting in 5 seconds", end="")
        for point in ".....":
            print(point, end="", flush=True)
            time.sleep(1)

if __name__ == "__main__":
    initialize_database()
    main()
    exit_message()
