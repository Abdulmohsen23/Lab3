print('Please enter 10 numbers:')
numbers = []
counter = 1

while (counter <= 10):
    try:
        numbers.append(int(input(f'Number {counter}:')))
        counter +=1
    except ValueError:
        print('Error: please enter a valid numrical number')
        
numbers.sort()
print(f'The largest number is {numbers[len(numbers)-1]}')