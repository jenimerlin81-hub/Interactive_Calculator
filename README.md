# Interactive Calculator & Unit Converter

A beginner-friendly Python CLI application that performs basic arithmetic operations, currency conversion, and unit conversions.

## 📌 Project Overview

The **Interactive Calculator & Unit Converter** is a command-line application developed using Python.

The program allows users to:

* Perform basic arithmetic operations
* Convert kilometers to miles
* Convert Celsius to Fahrenheit
* Convert USD to INR
* Convert INR to USD
* Handle invalid user inputs
* Continue using the application until the user chooses to exit

This project is designed to practice fundamental Python concepts such as functions, conditionals, loops, user input, and exception handling.

## ✨ Features

### 1. Basic Arithmetic

The calculator supports:

* Addition
* Subtraction
* Multiplication
* Division

It also handles division-by-zero errors.

### 2. Unit Conversion

The application supports:

* Kilometers to Miles
* Celsius to Fahrenheit

### 3. Currency Conversion

The application supports:

* USD to INR
* INR to USD

A fixed sample exchange rate is used:

```text
1 USD = 83 INR
```

> Note: The currency exchange rate is fixed for this beginner project and is not a live exchange rate.

### 4. Input Validation

The program validates user input using:

* `while` loops
* `try-except`
* `if-else` conditions

Invalid numeric input is handled without crashing the program.

## 🛠️ Technologies Used

* Python 3
* Command Line Interface (CLI)

## 📂 Project Structure

```text
Interactive_Calculator/
│
├── calculator.py
└── README.md
```

## 🧠 Python Concepts Used

This project demonstrates:

* Variables
* Data Types
* `input()`
* `print()`
* `if`, `elif`, `else`
* `while` loops
* `break`
* Functions
* `try-except`
* Arithmetic operators
* Type conversion using `float()`
* Basic error handling

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your system.

Check the Python version:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/Interactive_Calculator.git
```

### Step 3: Open the Project Folder

```bash
cd Interactive_Calculator
```

### Step 4: Run the Program

```bash
python calculator.py
```

## 💻 Sample Output

```text
==========================================
   INTERACTIVE CALCULATOR & CONVERTER
==========================================

1. Basic Arithmetic
2. Unit Conversion
3. Currency Conversion
4. Exit

Enter your choice: 1

===== Basic Arithmetic =====
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Back to Main Menu

Enter your choice: 1
Enter first number: 10
Enter second number: 20

Result: 30.0
```

## 📐 Conversion Formulas

### Kilometers to Miles

```text
Miles = Kilometers × 0.621371
```

### Celsius to Fahrenheit

```text
Fahrenheit = (Celsius × 9/5) + 32
```

### USD to INR

```text
INR = USD × 83
```

### INR to USD

```text
USD = INR / 83
```

## 🎯 Learning Outcomes

After completing this project, you will understand:

* How to create Python functions
* How to take user input
* How to use conditional statements
* How to use `while` loops
* How to validate user input
* How to handle errors using `try-except`
* How to build a simple CLI application
* How to organize a beginner-level Python project

## 🚀 Future Improvements

The project can be enhanced by adding:

* More unit conversions
* More currencies
* Live currency exchange rates
* Length, weight, and temperature conversions
* Calculation history
* A graphical user interface (GUI)
* Better input validation
* More arithmetic operations

## 👩‍💻 Author

**Jeni Merlin**

AI & Data Science Student

## 📄 License

This project is created for educational and learning purposes.
