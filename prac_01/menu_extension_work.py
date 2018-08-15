Menu = """ H- Hello
G- Goodbye
Q- Quit"""
print(Menu)
choice = input(">>>").upper()

while choice != "Q":
    if choice == "H":
        print("Hello Guido")
    elif choice == "G":
        print("Goodbye Guido")
    else:
        print("Invalid Option")
    print(Menu)
    choice = input(">>>").upper()
print("Cheers")
