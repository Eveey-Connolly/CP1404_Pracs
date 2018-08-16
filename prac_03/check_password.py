MINIMUM_LENGTH = 3


def main():
     password = input("Enter Password:")
     get_password(MINIMUM_LENGTH, password)
     asterisk_printer(password)


def get_password(min_length, password):
    while len(password) < min_length:
        print("Invalid Password Length")
        password = input("Enter Password:")
    return password


def asterisk_printer(password):
    for i in range(0, len(password)):
        print("*", end="")


main()
