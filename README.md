# JCDS-2602 Module 1 Capstone Project: Car Rental System

## 1. Background

A streamlined car rental service requires a well-structured and automated system to track vehicle availability, process rentals and returns, and generate invoices. This capstone project focuses on developing a simple and user-friendly car rental system with complete CRUD (Create, Read, Update, Delete) functionality to optimize rental operations and enhance the overall customer experience.

## 2. Objectives

The aim of this project is to develop a fully functional car rental system designed for two user roles:

### Customers can:
- View available cars.
- Rent an available car.
- View invoices for completed rentals.

### Administrators can:
- Manage the car inventory (add, update, or remove cars).
- Keep track of rental transactions.

## 3. Requirements Analysis

### Functional Requirements

- View available and rented cars.
- View cars in a sorted manner, either by `Brand`, `Model`, or `Price`.
- Add, update, and remove cars from the fleet.
- Rent a car and track its status.
- Return a rented car and update its availability.
- Generate an invoice upon approval of the rental.
- View invoices by entering the car’s registration number.

## 4. System Design

### Data Structure

The system uses a list of dictionaries to store car information. Each dictionary contains:

- **Registration No.**: (Integer) Unique ID of the car.
- **Brand**: (String) Car brand.
- **Model**: (String) Car model.
- **Type**: (String) Car type (SUV or Sedan).
- **Year**: (Integer) Manufacturing year.
- **Price**: (Integer) Rental price per day.
- **Status**: (String) Availability status (Available or Rented).

### Invoice Data Structure

- **Registration No.**: (Integer) Unique car ID.
- **Brand**: (String) Car brand.
- **Model**: (String) Car model.
- **Year**: (Integer) Manufacturing year.
- **Price**: (Integer) Rental price per day.
- **Payment**: (Integer) Total payment received.
- **Change**: (Integer) Change from the payment, if any.

## 5. CRUD Functions

### Core Functionalities

- **display_all_cars()** – Displays the list of all available and rented cars.
- **add_car()** – Adds a new car to the fleet.
- **update_car()** – Updates details of an existing car.
- **delete_car()** – Removes a car from the inventory (if not rented).
- **rent_car()** – Marks a car as rented and updates its status.
- **return_car()** – Marks a car as returned and updates its status.
- **generate_invoice()** – Creates an invoice upon rental approval.
- **check_invoice()** – Allows the user to view their invoices by entering the registration number.
- **sort_cars()** – Sorts the list of cars based on brand, model, or price.
- **clear()** – Clears the screen to improve the user experience.
- **main()** – The backbone of the car rental system, responsible for displaying the main menu.

## 6. Libraries Used

- **tabulate** – Formats and displays car lists and invoices in a tabular format.
- **os & platform** – Used to fetch system information and create a function that clears the console throughout different stages while the program runs.

## 7. User Manual
1. Install dependencies: `pip install tabulate`
2. Ensure that Python is installed.
3. Run the program.
4. Navigate through the program according to the instructions displayed.
5. If prompted for a password, enter `123`.

## 8. Disclaimer
- The `clear()` function was specifically designed for Windows devices to clear the terminal and improve UI/UX. If you are using a different operating system, remove or modify this function before running the program.

---

<em>Adrian Irshad</em>

<em>JCDS 2602, Purwadhika Digital Technology School, BSD</em>

<em>2025</em>
