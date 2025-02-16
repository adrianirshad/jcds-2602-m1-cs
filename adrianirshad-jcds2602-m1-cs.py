# JCDS-2602 Module 1 Capstone Project: Car Rental System


# Import libraries
import os
import platform
from tabulate import tabulate 

# Function to clear the terminal where needed
# Remove or modify this function if you are not using a windows device
# Or else the program will not able to run
def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Initial dataset of cars
cars = [
    {"Registration No.": 260201, "Brand": "Toyota", "Model": "Land Cruiser", "Type": "SUV", "Year": 2024, "Price": 450, "Status": "Rented"},
    {"Registration No.": 260202, "Brand": "Nissan", "Model": "Patrol", "Type": "SUV", "Year": 2025, "Price": 400, "Status": "Available"},
    {"Registration No.": 260203, "Brand": "Lexus", "Model": "LX", "Type": "SUV", "Year": 2025, "Price": 480, "Status": "Available"},
    {"Registration No.": 260204, "Brand": "Land Rover", "Model": "Defender", "Type": "SUV", "Year": 2020, "Price": 350, "Status": "Available"},
    {"Registration No.": 260205, "Brand": "Jetour", "Model": "T2", "Type": "SUV", "Year": 2023, "Price": 250, "Status": "Rented"},
    {"Registration No.": 260206, "Brand": "Mercedes-Benz", "Model": "G-Class", "Type": "SUV", "Year": 2024, "Price": 500, "Status": "Rented"},
    {"Registration No.": 260207, "Brand": "BMW", "Model": "7-Series", "Type": "Sedan", "Year": 2022, "Price": 380, "Status": "Available"},
    {"Registration No.": 260208, "Brand": "Mercedes-Benz", "Model": "S-Class", "Type": "Sedan", "Year": 2020, "Price": 420, "Status": "Rented"},
    {"Registration No.": 260209, "Brand": "Genesis", "Model": "G90", "Type": "Sedan", "Year": 2025, "Price": 320, "Status": "Available"}
]

# Create an empty list to store invoices after rental approvals
invoices = []

# Function to check if the user knows the password (under the assumption that some functionalities are only available to admins)
def check_pass():
    clear()
    password = "123"
    
    while True:
        pw = input("\nPlease enter the password: ")

        if pw == password:
            clear()
            print("\nAccess granted!")
            return True
        else:
            clear()
            print("\nIncorrect password! Please try again.")

# Function to ask user whether or not they are an admin
def check_admin():
    while True:
        is_admin = input("\nAre you an admin? (Yes/No): ").strip().lower()

        if is_admin == "yes":
            return check_pass()
        elif is_admin == "no":
            clear()
            print("The current function is only available for system admins.")
            return main()
        else:
            clear()
            print("Invalid input! Please enter 'Yes' or 'No'.")

# Function to ask the user if they are of legal age to be renting a car
def check_age():
    while True:
        age = input("\nAre you above 18 years old? (Yes/No): ").strip().lower()
        
        if age == "yes":
            clear()
            return True
        elif age == "no":
            clear()
            print("\nYou must be at least 18 years old to rent a car.")
            return False
        else:
            clear()
            print("\nInvalid input! Please enter 'Yes' or 'No'.")

# Function to ask user if they have a license which is required to rent a car
def check_license():
    while True:
        check_license = input("\nDo you have a valid driving license? (Yes/No): ").strip().lower()

        if check_license == "yes":
            clear()
            return True
        elif check_license == "no":
            clear()
            print("\nYou must have a valid driving license to rent a car.")
            return False
        else:
            clear()
            print("\nInvalid input! Please enter 'Yes' or 'No'.")

# Function to check the invoice of the car registration mentioned by the user, if existing
def check_invoice():
    while True:
        try:
            if not display_rented_cars():
                return
            
            reg_no = int(input("\nEnter the Registration Number to view the invoice (press 0 to cancel): "))
            if reg_no == 0:
                clear()
                print("Invoice lookup canceled.")
                return
            
            invoice_found = False
            for invoice in invoices:
                if invoice["Registration No."] == reg_no:
                    clear()
                    print("Here is the invoice for Registration Number: {}".format(reg_no))
                    print(tabulate([invoice], headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))
                    invoice_found = True
                    input("\nPress Enter to continue...")
                    clear()
                    return
            
            if not invoice_found:
                clear()
                print("\nNo invoice found for the given Registration Number. Please try again.\n")
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a numeric Registration Number.\n")

# Function to display all cars from the dataset, whether available or rented
def display_all_cars():
    if not cars:
        print("There are currently no cars available for rent.")
        return
    
    print(tabulate(cars,
                   headers="keys",
                   tablefmt="fancy_grid",
                   colalign=(('center',) * 7)
                   ))

# Function to display only the cars which are currently available
def display_available_cars():
    available_cars = [car for car in cars if car["Status"] == "Available"]
    
    if not available_cars:
        print("There are currently no cars available for rent.")
        return
    
    print("\nBelow are the cars currently available for rent: ")
    print(tabulate(available_cars,
                   headers="keys",
                   tablefmt="fancy_grid",
                   colalign=(('center',) * 7)))

# Function to display only the cars which are currently being rented
def display_rented_cars():
    rented_cars = [car for car in cars if car["Status"] == "Rented"]
    
    if not rented_cars:
        print("There are currently no cars being rented out.")
        input("\nPress Enter to continue...")
        clear()
        return False
    
    print("Below are the cars currently being rented out:")
    print(tabulate(rented_cars,
                   headers="keys",
                   tablefmt="fancy_grid",
                   colalign=(('center',) * 7)))
    
    return True

# Function to sort all cars by price, from lowest to highest
def sort_cars_lowhigh():
    sorted_cars_lowhigh = sorted(cars, key=lambda x: x["Price"])
    print(tabulate(sorted_cars_lowhigh, headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))

# Function to sort all cars by price, from highest to lowest
def sort_cars_highlow():
    sorted_cars_highlow = sorted(cars, key=lambda x: x["Price"], reverse=True)
    print(tabulate(sorted_cars_highlow, headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))

# Function to sort all cars by name from A-Z, mainly by brand, model, and then type
def sort_cars_nameasc():
    sorted_cars_nameasc = sorted(cars, key=lambda x: (x["Brand"], x["Model"], x["Type"]))
    print(tabulate(sorted_cars_nameasc, headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))

# Function to sort all cars by name from Z-A, mainly by brand, model, and then type
def sort_cars_namedesc():
    sorted_cars_namedesc = sorted(cars, key=lambda x: (x["Brand"], x["Model"], x["Type"]), reverse=True)
    print(tabulate(sorted_cars_namedesc, headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))

# Function to display the menu for choice number 1
def display_cars_menu():
    clear()
    while True:
        print("\nAdrian's Car Rental")
        print("1. View all cars")
        print("2. Sort all cars")
        print("3. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1, 2, or 3): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter 1,2, or 3.")
            continue

        clear()

        if choice == 1:
            display_all_cars()
            input("\nPress Enter to continue...")
            clear()
            return display_cars_menu()
        elif choice == 2:
            clear()
            display_cars_menu_sort()
        elif choice == 3:
            return  
        else:
            clear()
            print("\nInvalid choice. Please enter 1,2, or 3.")

# Function to display the sub-menu from choice number 1, with different sorting options
def display_cars_menu_sort():
    clear()
    while True:
        print("\nAdrian's Car Rental")
        print("1. Sort from lowest to highest price")
        print("2. Sort from highest to lowest price")
        print("3. Sort by brand from A-Z")
        print("4. Sort by brand from Z-A")
        print("5. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1-5): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter a number from 1 to 5.")
            continue

        clear()

        if choice == 1:
            sort_cars_lowhigh()
            input("\nPress Enter to continue...")
            clear()
            return display_cars_menu_sort()
        elif choice == 2:
            sort_cars_highlow()
            input("\nPress Enter to continue...")
            clear()
            return display_cars_menu_sort()            
        elif choice == 3:
            sort_cars_nameasc()
            input("\nPress Enter to continue...")
            clear()
            return display_cars_menu_sort() 
        elif choice == 4:
            sort_cars_namedesc()
            input("\nPress Enter to continue...")
            clear()
            return display_cars_menu_sort() 
        elif choice == 5:
            return
        else:
            clear()
            print("\nInvalid choice. Please enter a number from 1 to 5.")   

# Function to ask the user for payment and to ensure that the amount is no less than the total price
def payment(total_price):
    while True:
        try:
            amount_received = int(input(f"\nTotal price is ${total_price}. Enter amount to pay: "))
            
            if amount_received >= total_price:
                return amount_received
            else:
                clear()
                print("\nInsufficient funds! Your payment is short of ${}.".format(total_price - amount_received))
        
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a valid numeric amount.")

# Function to display the menu for choice number 2
def rent_car_menu():
    while True:
        print("\nAdrian's Car Rental")
        print("1. Rent a car")
        print("2. View invoice")
        print("3. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1, 2, or 3): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter 1,2, or 3.")
            continue  

        clear()

        if choice == 1:
            display_available_cars()
            rent_car()
        elif choice == 2:
            check_invoice()
        elif choice == 3:
            return  
        else:
            print("\nInvalid choice. Please enter 1,2, or 3.")

# Function to allow the users to rent a car and complete the payment process
def rent_car():
    clear()
    
    if not check_age():
        return
    
    if not check_license():
        return  
    
    while True:
        display_available_cars()
        
        try:
            reg_no = int(input("\nEnter the Registration Number of the car you would like to rent (press 0 to cancel): "))

            if reg_no == 0:
                clear()
                print("\nRental process has been cancelled.")
                return

            for car in cars:
                if car["Registration No."] == reg_no and car["Status"] == "Available":
                    total_price = car["Price"]
                    
                    amount_received = payment(total_price)
                    
                    if amount_received >= total_price:
                        change = amount_received - total_price
                        car["Status"] = "Rented"

                        invoice = {
                            "Registration No.": car["Registration No."],
                            "Brand": car["Brand"],
                            "Model": car["Model"],
                            "Year": car["Year"],
                            "Price": total_price,
                            "Payment": amount_received,
                            "Change": change
                        }
                        invoices.append(invoice)

                        clear()
                        print("\nYou have successfully rented the {} {}!".format(car['Brand'], car['Model']))
                        print("\nHere is your invoice:")
                        print(tabulate([invoice], headers="keys", tablefmt="fancy_grid", colalign=(('center',) * 7)))
                        return
                    else:
                        clear()
                        print("\nInsufficient payment! Please enter an amount equal to or greater than the rental price.")
            
            clear()
            print("\nInvalid input! Please enter a valid Registration Number from the available cars.")
        
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a numeric Registration Number.")

# Function to display the menu for choice number 3
def return_car_menu():
    if not check_admin():
        return

    while True:
        print("\nAdrian's Car Rental")
        print("1. Return a car")
        print("2. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1 or 2): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter 1 or 2.")
            continue  

        clear()

        if choice == 1:
            return_car()
        elif choice == 2:
            break  
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
 
# Function to return a rented car, and update the status accordingly
def return_car():
    clear()
    
    if not display_rented_cars():
        return
    
    while True:
        try:
            reg_no = int(input("\nEnter the Registration Number of the car you would like to return (press 0 to cancel): "))

            if reg_no == 0:
                clear()
                print("\nReturn process has been cancelled.")
                return

            for car in cars:
                if car["Registration No."] == reg_no and car["Status"] == "Rented":
                    car["Status"] = "Available"

                    global invoices
                    invoices = [inv for inv in invoices if inv["Registration No."] != reg_no]

                    clear()
                    print(f"\nThe {car['Brand']} {car['Model']} has been successfully returned!\n")
                    display_rented_cars()
                    return
            
            clear()
            print("\nInvalid input! Please enter a valid Registration Number from the rented cars.\n")
            display_rented_cars()
            
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a numeric Registration Number.\n")
            display_rented_cars()

# Function to display the menu for choice number 4
def add_car_menu():
    if not check_admin():
        return
    
    while True:
        print("\nAdrian's Car Rental")
        print("1. Add a car")
        print("2. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1 or 2): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter 1 or 2.")
            continue  

        clear()

        if choice == 1:
            add_car()
        elif choice == 2:
            return  
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

# Function to add a car to the main dataset of cars, automatically sets status to 'Available'
def add_car():
    clear()
    
    print("Below are the cars currently in the fleet:\n")
    display_all_cars()
    print("\nPlease fill out the details of the new car:\n")

    existing_reg_no = {car["Registration No."] for car in cars}
    add_reg_no = max(existing_reg_no, default=260200) + 1

    while add_reg_no in existing_reg_no:
        add_reg_no += 1

    add_brand = input("Enter the car brand: ").strip().title()
    add_model = input("Enter the car model: ").strip().title()

    while True:
        try:
            add_car_type = input("Enter the car type (SUV or Sedan): ").strip().lower()
            if add_car_type == "suv":
                add_car_type = "SUV"
            elif add_car_type == "sedan":
                add_car_type = "Sedan"
            else:
                raise ValueError
            break
        except ValueError:
            clear()
            print("\nInvalid input! Please enter either 'SUV' or 'Sedan'.\n")

    while True:
        try:
            add_year = int(input("Enter the car's manufacturing year (1990-2025): "))
            if 1990 <= add_year <= 2025:
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a year between 1990 and 2025.\n")

    while True:
        try:
            add_price = int(input("Enter the rental price per day (100 - 500): "))
            if 100 <= add_price <= 500:
                break
            else:
                raise ValueError
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a price between 100 and 500.\n")

    add_status = "Available"

    new_car = {
        "Registration No.": add_reg_no,
        "Brand": add_brand,
        "Model": add_model,
        "Type": add_car_type,
        "Year": add_year,
        "Price": add_price,
        "Status": add_status
    }

    print("\nBelow are the details of the new car:")
    print(tabulate([new_car],
                   headers="keys",
                   tablefmt="fancy_grid",
                   colalign=(('center',) * 7)))

    while True:
        add_confirm = input("\nWould you like to confirm the new addition? (Yes/No): ").strip().lower()
        if add_confirm == "yes":
            cars.append(new_car)
            clear()
            print(f"\n{new_car['Brand']} {new_car['Model']} has been successfully added to the fleet!")
            print("\nHere is the updated fleet of cars:")
            display_all_cars()
            break
        elif add_confirm == "no":
            clear()
            print("\nThe process has been cancelled.")
            break
        else:
            clear()
            print("\nInvalid input! Please enter 'Yes' or 'No'.")

# Function to dispay to the menu for chouce number 5
def remove_car_menu():
    if not check_admin():
        return
    
    while True:
        print("\nAdrian's Car Rental")
        print("1. Remove a car")
        print("2. Return to main menu")

        try:
            choice = int(input("\nPlease enter your choice (1 or 2): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter 1 or 2.")
            continue  

        clear()

        if choice == 1:
            remove_car()
        elif choice == 2:
            return  
        else:
            print("\nInvalid choice. Please enter 1 or 2.")

# Function to remove a car from the main dataset of cars, by entering the registration no
def remove_car():
    clear()
    
    while True:
        display_all_cars()
        
        try:
            reg_no = int(input("\nEnter the Registration Number of the car you want to remove (press 0 to cancel): "))
            
            if reg_no == 0:
                clear()
                print("\nCar removal process has been cancelled.")
                return
            
            for car in cars:
                if car["Registration No."] == reg_no:
                    if car["Status"] == "Rented":
                        clear()
                        print("\nThis car is currently rented and cannot be removed.")
                        return
                    
                    while True:
                        confirm = input(f"\nAre you sure you want to remove the {car['Brand']} {car['Model']} (Reg No. {car['Registration No.']})? (Yes/No): ").strip().lower()
                        if confirm == "yes":
                            cars.remove(car)
                            clear()
                            print(f"\n{car['Brand']} {car['Model']} (Reg No. {car['Registration No.']}) has been successfully removed from the fleet!")
                            return
                        elif confirm == "no":
                            clear()
                            print("\nCar removal has been cancelled.")
                            return
                        else:
                            clear()
                            print("\nInvalid input! Please enter 'Yes' or 'No'.")
            
            clear()
            print("\nInvalid Registration Number! Please enter a valid number from the list.\n")
        
        except ValueError:
            clear()
            print("\nInvalid input! Please enter a numeric Registration Number.\n")

# Function to display the initial main menu and the different functionalities within this system
def main():
    while True:
        print("\nAdrian's Car Rental")
        print("1. View all cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Add a car")
        print("5. Remove a car")
        print("6. Exit")

        try:
            choice = int(input("\nPlease enter your choice (1-6): "))
        except ValueError:
            clear()
            print("\nInvalid input. Please enter a number between 1 and 6.")
            continue  

        clear()

        if choice == 1:
            display_cars_menu()
        elif choice == 2:
            rent_car_menu()  
        elif choice == 3:
            return_car_menu()
        elif choice == 4:
            add_car_menu()
        elif choice == 5:
            remove_car_menu()
        elif choice == 6:
            print("Thank you for visiting Adrian's Car Rental. Please visit again!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

# Clears the terminal everytime the code is run to make for a better user experience.
# The clear() function is used multiple times throughout the program too 
clear()
# Displays the main menu once the program starts.
main()

