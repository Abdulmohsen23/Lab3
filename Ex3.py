def celsius_to_fahrenheit(C):
    F = (9/5) * C + 32 
    return F

try:
    C = float(input('Please enter Celsius temperature: '))
    F = celsius_to_fahrenheit(C)
    print(f'Fahrenheit temperature is {F} F')
except ValueError:
    print('Error: please enter a valid numrical number')
