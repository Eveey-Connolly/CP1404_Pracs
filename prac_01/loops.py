
for i in range(1, 21, 2):
    print(i, end=' ')
print()
print('Count from 0 to 100')
for i in range(0, 101, 10):
    print(i, end=' ')
print()
print('Countdown from 20 to 1')
for i in reversed(range(0, 21, 1)):
    print(i, end=' ')
print()

number_of_stars = int(input('Number of Stars:'))
print('Number of Stars')
for i in range(number_of_stars):
    print('*', end='')

print()
print('Stars in Increasing Order on Each Line')
for i in range(-1, number_of_stars):
    print('*' * (i+1), end='')
    print()
print()
