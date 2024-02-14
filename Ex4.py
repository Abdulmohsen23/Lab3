def number_multiplication (num):
    for i in range(1,11):
        print(f'{num} * {i} = {i * num}')
try:
    number_multiplication(int(input('Enter the number: ')))
except ValueError:
    print('Error: please enter a valid numrical number')    