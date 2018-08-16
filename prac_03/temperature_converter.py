def celsius_to_fahrenheit():
    """Converts Celsius to Fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit:"))
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        print("Result: {:.2f} F".format(celsius_to_fahrenheit()))
        print(MENU)
        choice = input(">>> ").upper()
    elif choice == "F":
        print("Result:{:.2f}C".format(fahrenheit_to_celsius()))
        print(MENU)
        choice = input(">>> ").upper()
    else:
        print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
print("Thank you.")
