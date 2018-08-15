# Writes Name to File
OUT_FILE = "name.txt"
out_file = open(OUT_FILE, 'w')
name = input("Please enter your name:")

print(name, file=out_file)
out_file.close()

# Reads name from name.txt and prints it on console

out_file_2 = open(OUT_FILE, 'r')
name_in_file = out_file_2.read().strip()
print("Your name is", name_in_file)
out_file_2.close()

# Reads numbers in text and totals them
# number_file = open("numbers", "r")
# first_number = int(number_file.readline())
# second_number = int(number_file.readline())
# total = first_number + second_number
# print(total)
# number_file.close()

number_file_2 = open("numbers", "r")
total = 0
for number in number_file_2:
    number = int(number)
    total += number
print(total)
number_file_2.close()
