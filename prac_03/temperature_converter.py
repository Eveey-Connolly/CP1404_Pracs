def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        temperature = float(input("Temperature:"))
        if choice == "C":
            print("Result: {:.2f} F".format(celsius_to_fahrenheit(temperature)))
            print(MENU)
            choice = input(">>> ").upper()
        elif choice == "F":
            print("Result:{:.2f}C".format(fahrenheit_to_celsius(temperature)))
            print(MENU)
            choice = input(">>> ").upper()
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(temmperature):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = temmperature * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_to_celsius(temperature):

    celsius = (temperature - 32) * 5 / 9
    return celsius


main()
