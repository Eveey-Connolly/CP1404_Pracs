Menu = """E- Even Numbers
O-Odd Numbers
S- Square Numbers
Q- Quit"""

print(Menu)
choice = input(">>>").upper()
X_NUMBER = int(input("What is your X number?"))
Y_NUMBER = int(input("What is your y number?"))
while choice != "Q":
    if choice == "E":
        for i in range(X_NUMBER, Y_NUMBER):
            if i % 2:
                number = i
                print(i)
            else:
                print("no")