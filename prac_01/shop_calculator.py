number_of_items = int(input('Number of Items:'))
total = 0
while number_of_items < 0:
    print('Invalid Number of Items')
    number_of_items = int(input('Number of Items:'))

for i in range(number_of_items):
        price_of_item = float(input('Price of Item:'))
        total = total + price_of_item

if total > 100:
    total = total - (total * 0.1)
print("${:.2f}".format(total))
