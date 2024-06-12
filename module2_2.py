first = int(input('Enter a first number: '))
second = int(input('Enter a second number: '))
third = int(input('Enter a third number: '))

if first == second and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)